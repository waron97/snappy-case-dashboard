'use client';

import { Badge } from '@mantine/core';
import type { InitStatus, PreCommitStatus, PrRecord, TaskName, TaskState, TestStatus } from '@app/devops/actions';

/** Display order of the tasks, and the canonical runtime list of them. */
const TASK_NAMES: TaskName[] = ['tests', 'precommit', 'init'];

const TASK_LABEL: Record<TaskName, string> = {
    tests: 'tests',
    precommit: 'pre-commit',
    init: 'init',
};

/** Chip colour identifying the task itself, used while it is queued or running. */
const TASK_COLOR: Record<TaskName, string> = {
    tests: 'blue',
    precommit: 'grape',
    init: 'orange',
};

/**
 * The result a finished task produced. Each task reports its own — in particular
 * `pr.status` is NOT usable for `tests`, because it reads "running" whenever any task
 * of the commit is running. `null` means the task finished without a parseable result,
 * an infra failure worth surfacing rather than hiding.
 */
function resultFor(task: TaskName, pr: PrRecord | null): TestStatus | PreCommitStatus | InitStatus | null {
    if (!pr) {
        return null;
    }
    if (task === 'tests') {
        return pr.testStatus;
    }
    if (task === 'precommit') {
        return pr.preCommitStatus;
    }
    return pr.initStatus;
}

const GOOD = ['passed', 'ok', 'done'];
const BAD = ['failed', 'unknown', 'ko'];

export function TaskBadge({
    task,
    state,
    pr,
}: {
    task: TaskName;
    state: TaskState | undefined;
    pr: PrRecord | null;
}) {
    if (!state) {
        return (
            <TaskChip color="gray" variant="outline">
                {TASK_LABEL[task]} —
            </TaskChip>
        );
    }

    if (state === 'queued' || state === 'running') {
        return (
            <TaskChip
                color={state === 'running' ? TASK_COLOR[task] : 'gray'}
                variant={state === 'running' ? 'filled' : 'light'}
            >
                {TASK_LABEL[task]} {state}
            </TaskChip>
        );
    }

    const result = resultFor(task, pr);
    const color = result && GOOD.includes(result) ? 'green' : result && BAD.includes(result) ? 'red' : 'orange';
    return (
        <TaskChip color={color} variant="light">
            {TASK_LABEL[task]} {result ?? 'not run'}
        </TaskChip>
    );
}

/**
 * Badge truncates its label to an ellipsis by default, which made these unreadable in
 * the narrow PR-list status cell. Keep the text intact and lower-case — "pre-commit ko"
 * reads faster than "PRE-COMMI…".
 */
function TaskChip({
    color,
    variant,
    children,
}: {
    color: string;
    variant: string;
    children: React.ReactNode;
}) {
    return (
        <Badge
            color={color}
            variant={variant}
            size="sm"
            tt="none"
            styles={{ label: { overflow: 'visible' } }}
        >
            {children}
        </Badge>
    );
}

export { TASK_COLOR, TASK_LABEL, TASK_NAMES };
