import { useEffect, useState } from 'react';
import { python } from '@codemirror/lang-python';
import { vim } from '@replit/codemirror-vim';
import { IconLock, IconLockX } from '@tabler/icons-react';
import { useQuery, useQueryClient } from '@tanstack/react-query';
import { vscodeDark } from '@uiw/codemirror-theme-vscode';
import ReactCodeMirror from '@uiw/react-codemirror';
import { toast, ToastContainer } from 'react-toastify';
import { Alert, Button, Center, Group, Select, Stack, Text } from '@mantine/core';
import { odooCallMethod, odooRead, odooSearchRead, odooWrite, OneToMany } from '../../../app/api';
import UiCard from '../UiCard';

type Props = {
  caseId: number;
  workflowId?: number;
  activePhaseId?: number;
};

export default function CaseActivePhase(props: Props) {
  const { caseId, workflowId } = props;

  // -------------------------------------
  // Hooks
  // -------------------------------------

  const [isLocked, setIsLocked] = useState(true);

  const [form, setForm] = useState<{ phase: number | null; code: string }>({
    phase: null,
    code: '',
  });

  const queryClient = useQueryClient();

  // -------------------------------------
  // Queries
  // -------------------------------------

  const { data: [caseFields] = [] } = useQuery<{ triplet_active_phase_id: OneToMany }[]>({
    queryKey: ['case', caseId, 'for-active-phase'],
    refetchInterval: isLocked ? 3 * 1000 : undefined,
    queryFn: () => odooRead('helpdesk.ticket', [caseId], ['triplet_active_phase_id']),
  });

  const { data: workflowPhases } = useQuery<{ id: number; name: string }[]>({
    queryKey: ['workflow', 'phases', { workflowId }],
    enabled: !!workflowId,
    queryFn: () =>
      odooSearchRead('symple.triplet.phase', [['workflow_id', '=', workflowId!]], ['id', 'name']),
  });

  const activePhaseId = caseFields?.triplet_active_phase_id?.[0];

  const { data: [activePhaseData] = [] } = useQuery<
    {
      id: number;
      code: string;
      set_result_automatically: string;
    }[]
  >({
    queryKey: ['phase', activePhaseId, 'for-active-phase'],
    enabled: !!activePhaseId,
    queryFn: () =>
      odooRead('symple.triplet.phase', [activePhaseId], ['code', 'set_result_automatically']),
  });

  const phaseIdToFetch = form.phase;

  const { data: [selectedPhaseData] = [] } = useQuery<
    {
      id: number;
      code: string;
      set_result_automatically: string;
    }[]
  >({
    queryKey: ['phase', phaseIdToFetch, 'for-active-phase'],
    enabled: !!phaseIdToFetch,
    queryFn: () =>
      odooRead('symple.triplet.phase', [phaseIdToFetch!], ['code', 'set_result_automatically']),
  });

  const [submitting, setSubmitting] = useState(false);
  const [relaunching, setRelaunching] = useState(false);

  // -------------------------------------
  // Effects
  // -------------------------------------

  useEffect(() => {
    if (caseFields) {
      setForm({ ...form, phase: caseFields.triplet_active_phase_id[0] });
    }
  }, [caseFields]);

  useEffect(() => {
    if (selectedPhaseData) {
      setForm({ ...form, phase: selectedPhaseData.id, code: selectedPhaseData.code });
    }
  }, [selectedPhaseData]);

  // -------------------------------------
  // Functions
  // -------------------------------------

  async function submit() {
    setSubmitting(true);
    try {
      await odooWrite(
        'helpdesk.ticket',
        [caseId],
        { triplet_phase_id: form.phase },
        { bypass_ticket_check_write_allowed: true }
      );
      setIsLocked(true);
      queryClient.invalidateQueries({ queryKey: ['case', caseId, 'for-active-phase'] });
      queryClient.invalidateQueries({ queryKey: ['phase', form.phase, 'for-active-phase'] });
      queryClient.invalidateQueries({ queryKey: ['case-history', caseId] });
    } catch (err) {
      if (err instanceof Error) {
        toast(err.message);
        // eslint-disable-next-line
        console.error(err);
      } else {
        toast('Unknown error. Check browser console.');
        // eslint-disable-next-line
        console.error(err);
      }
    } finally {
      setSubmitting(false);
    }
  }

  async function relaunch() {
    setRelaunching(true);
    try {
      await odooCallMethod('helpdesk.ticket', [caseId], 'run_code_and_set_result');
      queryClient.invalidateQueries({ queryKey: ['case', caseId, 'for-active-phase'] });
      queryClient.invalidateQueries({ queryKey: ['logs', caseId] });
    } catch (err) {
      if (err instanceof Error) {
        toast(err.message);
        // eslint-disable-next-line
        console.error(err);
      } else {
        toast('Unknown error. Check browser console.');
        // eslint-disable-next-line
        console.error(err);
      }
    } finally {
      setRelaunching(false);
    }
  }

  function handleLock() {
    if (isLocked) {
      setIsLocked(false);
    } else {
      setIsLocked(true);
      setForm({
        phase: caseFields.triplet_active_phase_id[0],
        code: activePhaseData?.code || '',
      });
    }
  }

  function getChangedFields() {
    const changed = {
      phase: false,
      code: false,
    };
    let anyChanged = false;

    if (isLocked) {
      return [false, changed];
    }

    if (form.phase !== caseFields?.triplet_active_phase_id?.[0]) {
      changed.phase = true;
      anyChanged = true;
    }
    if (selectedPhaseData?.code && form.code !== selectedPhaseData?.code) {
      changed.code = true;
      anyChanged = true;
    }

    return [anyChanged, changed];
  }

  function renderCodeEditor() {
    if (isLocked || !form.code || selectedPhaseData?.set_result_automatically !== 'from_code') {
      return null;
    }
    return (
      <>
        <ReactCodeMirror
          value={selectedPhaseData?.code || ''}
          readOnly={isLocked}
          theme={vscodeDark}
          extensions={[python(), vim()]}
          maxHeight="600px"
          basicSetup={{
            lineNumbers: true,
            foldGutter: true,
            highlightActiveLine: true,
            dropCursor: true,
            allowMultipleSelections: true,
            indentOnInput: true,
          }}
        />
      </>
    );
  }

  function renderContent() {
    if (!workflowId) {
      return (
        <Center>
          <Text c="red">Case has no workflow</Text>
        </Center>
      );
    }

    const [didFieldsChange] = getChangedFields();

    return (
      <Stack gap="md">
        {didFieldsChange && (
          <Alert color="yellow" mb="md" title="Unsaved changes">
            <Text size="sm">
              Data was changed. On save, code changes will be written and the ticket will be moved
              to the selected phase.
            </Text>
            <Group mt="sm" gap="xs">
              <Button size="xs" color="green" onClick={submit} loading={submitting}>
                Submit
              </Button>
              <Button
                size="xs"
                variant="subtle"
                onClick={() => {
                  setForm({
                    ...form,
                    phase: caseFields.triplet_active_phase_id[0],
                    code: '',
                  });
                }}
              >
                Reset
              </Button>
            </Group>
          </Alert>
        )}
        <Select
          label="Active phase"
          disabled={isLocked}
          searchable
          data={
            workflowPhases?.map((phase) => ({ label: phase.name, value: String(phase.id) })) || []
          }
          value={String(phaseIdToFetch)}
          onChange={(v) => setForm({ ...form, phase: v ? parseInt(v, 10) : null })}
        />
        {renderCodeEditor()}
      </Stack>
    );
  }

  // -------------------------------------
  // Local Variables
  // -------------------------------------

  // -------------------------------------

  return (
    <UiCard
      title="Active phase"
      rightElement={
        <Group gap="sm">
          <Button onClick={relaunch} loading={relaunching}>
            Relaunch phase
          </Button>
          <Button onClick={handleLock}>
            <Group gap="sm">
              <Text>{isLocked ? 'Unlock' : 'Lock'}</Text>
              {isLocked ? <IconLockX /> : <IconLock />}
            </Group>
          </Button>
        </Group>
      }
    >
      {renderContent()}
      <ToastContainer />
    </UiCard>
  );
}
