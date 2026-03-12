import { useEffect, useEffectEvent, useState } from 'react';
import { python } from '@codemirror/lang-python';
import { vim } from '@replit/codemirror-vim';
import { IconLock, IconLockX } from '@tabler/icons-react';
import { useQuery } from '@tanstack/react-query';
import { vscodeDark } from '@uiw/codemirror-theme-vscode';
import ReactCodeMirror from '@uiw/react-codemirror';
import { Button, Center, Group, Select, Stack, Text } from '@mantine/core';
import { odooRead, odooSearchRead, OneToMany } from '../../../app/api';
import UiCard from '../UiCard';

type Props = {
  caseId: number;
  workflowId?: number;
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

  // -------------------------------------
  // Queries
  // -------------------------------------

  const { data: [caseFields] = [] } = useQuery<{ triplet_active_phase_id: OneToMany }[]>({
    queryKey: ['case', { caseId }, 'for-active-phase'],
    refetchInterval: isLocked ? 3 * 1000 : undefined,
    queryFn: () => odooRead('helpdesk.ticket', [caseId], ['triplet_active_phase_id']),
  });

  const { data: workflowPhases } = useQuery<{ id: number; name: string }[]>({
    queryKey: ['workflow', 'phases', { workflowId }],
    enabled: !!workflowId,
    queryFn: () =>
      odooSearchRead('symple.triplet.phase', [['workflow_id', '=', workflowId!]], ['id', 'name']),
  });

  const phaseIdToFetch = form.phase;

  const { data: [activePhaseData] = [] } = useQuery<
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

  // -------------------------------------
  // Effects
  // -------------------------------------

  useEffect(() => {
    if (caseFields) {
      setForm({ ...form, phase: caseFields.triplet_active_phase_id[0] });
    }
  }, [caseFields]);

  useEffect(() => {
    if (activePhaseData) {
      setForm({ ...form, phase: activePhaseData.id, code: activePhaseData.code });
    }
  }, [activePhaseData]);

  // -------------------------------------
  // Functions
  // -------------------------------------

  function handleLock() {
    if (isLocked) {
      setIsLocked(false);
    } else {
      setIsLocked(true);
      setForm({
        phase: caseFields.triplet_active_phase_id[0],
        code: '',
      });
    }
  }

  function renderContent() {
    if (!workflowId) {
      return (
        <Center>
          <Text c="red">Case has no workflow</Text>
        </Center>
      );
    }
    return (
      <Stack gap="md">
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
        <ReactCodeMirror
          value={activePhaseData?.code || ''}
          readOnly={isLocked}
          theme={vscodeDark}
          extensions={[python(), vim()]}
          basicSetup={{
            lineNumbers: true,
            foldGutter: true,
            highlightActiveLine: true,
            dropCursor: true,
            allowMultipleSelections: true,
            indentOnInput: true,
          }}
        />
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
          <Button>Relaunch phase</Button>
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
    </UiCard>
  );
}
