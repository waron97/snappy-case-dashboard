import { useEffect, useRef, useState } from 'react';
import { json } from '@codemirror/lang-json';
import { vim, Vim } from '@replit/codemirror-vim';
import { vscodeDark } from '@uiw/codemirror-theme-vscode';
import ReactCodeMirror from '@uiw/react-codemirror';
import { Checkbox, Group, Stack, TagsInput } from '@mantine/core';
import { DateInput } from '@mantine/dates';

type Props = {
    value: { [key: string]: any };
    onChange: (v: { [key: string]: any }) => void;
    toDomain?: (filters: { [key: string]: any }) => any[];
};

export default function CaseFilters(props: Props) {
    const { value: filters, onChange: setFilters, toDomain } = props;

    // -------------------------------------
    // Hooks
    // -------------------------------------

    const [draft, setDraft] = useState<string>(filters.customDomain ?? '[]');

    const draftRef = useRef(draft);
    const filtersRef = useRef(filters);
    const setFiltersRef = useRef(setFilters);
    filtersRef.current = filters;
    setFiltersRef.current = setFilters;

    // -------------------------------------
    // Effects
    // -------------------------------------

    useEffect(() => {
        draftRef.current = draft;
    }, [draft]);

    useEffect(() => {
        Vim.defineEx('write', 'w', () => {
            setFiltersRef.current({ ...filtersRef.current, customDomain: draftRef.current });
        });
    }, []);

    // -------------------------------------
    // Functions
    // -------------------------------------

    // -------------------------------------
    // Local Variables
    // -------------------------------------

    // -------------------------------------

    return (
        <Stack gap="sm">
            {filters.useCustomDomain ? (
                <Stack>
                    <ReactCodeMirror
                        value={draft}
                        theme={vscodeDark}
                        extensions={[json(), vim()]}
                        onChange={(v) => setDraft(v)}
                        basicSetup={{ lineNumbers: true }}
                        minHeight="120px"
                    />
                    <Checkbox
                        label="Custom domain"
                        checked={filters.useCustomDomain === true}
                        onChange={(e) => {
                            if (e.target.checked) {
                                const domain = toDomain?.(filters) ?? [];
                                const domainStr = JSON.stringify(domain, null, 2);
                                setDraft(domainStr);
                                setFilters({
                                    ...filters,
                                    useCustomDomain: true,
                                    customDomain: domainStr,
                                });
                            } else {
                                setFilters({ ...filters, useCustomDomain: false });
                            }
                        }}
                    />
                </Stack>
            ) : (
                <>
                    <Group grow>
                        <TagsInput
                            label="Case Name"
                            value={filters.name}
                            onChange={(value: string[]) =>
                                setFilters({ ...filters, name: value || [] })
                            }
                        />
                        <TagsInput
                            label="Workflow"
                            value={filters.workflow}
                            onChange={(v) => setFilters({ ...filters, workflow: v })}
                        />
                        <TagsInput
                            label="Ticket type"
                            value={filters.ticketType}
                            onChange={(v) => setFilters({ ...filters, ticketType: v })}
                        />
                    </Group>
                    <Group grow>
                        <DateInput
                            label="Creati dopo il"
                            value={filters.startDate}
                            onChange={(v) => setFilters({ ...filters, startDate: v })}
                            clearable
                        />
                        <DateInput
                            label="Creati prima del"
                            value={filters.endDate}
                            onChange={(v) => setFilters({ ...filters, endDate: v })}
                            clearable
                        />
                    </Group>
                    <Group gap="sm">
                        <Checkbox
                            label="Mostra case chiusi"
                            checked={filters.is_close === null}
                            onChange={(v) =>
                                setFilters({
                                    ...filters,
                                    is_close: v.target.checked ? null : false,
                                })
                            }
                        />
                        <Checkbox
                            label="Custom domain"
                            checked={filters.useCustomDomain === true}
                            onChange={(e) => {
                                if (e.target.checked) {
                                    const domain = toDomain?.(filters) ?? [];
                                    const domainStr = JSON.stringify(domain, null, 2);
                                    setDraft(domainStr);
                                    setFilters({
                                        ...filters,
                                        useCustomDomain: true,
                                        customDomain: domainStr,
                                    });
                                } else {
                                    setFilters({ ...filters, useCustomDomain: false });
                                }
                            }}
                        />
                    </Group>
                </>
            )}
        </Stack>
    );
}
