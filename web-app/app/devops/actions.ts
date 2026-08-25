'use server';

import fs from 'fs/promises';
import path from 'path';
import Redis from 'ioredis';

const TESTRUNNER = process.env.TESTRUNNER_API_URL ?? 'http://auto-testrunner:8080';
const RESULTS = process.env.RESULTS_DIR ?? '/results';
const REDIS_URL = process.env.REDIS_URL ?? 'redis://redis:6379';

let _redis: Redis | null = null;
function getRedis(): Redis {
    if (!_redis) {
        _redis = new Redis(REDIS_URL);
    }
    return _redis;
}

export type PrStatus = 'passed' | 'failed' | 'unknown' | 'done' | 'running' | 'queued' | 'pending';

export type PreCommitStatus = 'ok' | 'ko';

export type InitStatus = 'ok' | 'ko';

/** The tests task's own result, independent of the commit-wide `status`. */
export type TestStatus = 'passed' | 'failed' | 'unknown' | 'done';

/**
 * A commit's work is split into these independently-queued tasks, one per worker.
 * Only types live here — this is a 'use server' module, so it may not export runtime
 * values other than async functions. See TASK_NAMES in @/components/TaskBadge.
 */
export type TaskName = 'tests' | 'precommit' | 'init';

export type TaskState = 'queued' | 'running' | 'done';

export type PrRecord = {
    id: number;
    title: string;
    author: string;
    sourceBranch: string;
    commitId: string;
    /** Commit-wide: reads 'running' when ANY task of the commit is running. */
    status: PrStatus;
    testStatus: TestStatus | null;
    preCommitStatus: PreCommitStatus | null;
    initStatus: InitStatus | null;
    tasks: Partial<Record<TaskName, TaskState>>;
    isDraft: boolean;
};

export async function fetchPrs(): Promise<PrRecord[]> {
    const res = await fetch(`${TESTRUNNER}/prs`, { cache: 'no-store' });
    if (!res.ok) {
        throw new Error(`/prs returned ${res.status}`);
    }
    return res.json();
}

export async function triggerDiscover(): Promise<{ prs_found: number; enqueued: string[] }> {
    const res = await fetch(`${TESTRUNNER}/discover`, { method: 'POST', cache: 'no-store' });
    if (!res.ok) {
        throw new Error(`/discover returned ${res.status}`);
    }
    return res.json();
}

export async function triggerRecheck(hash: string): Promise<void> {
    const res = await fetch(`${TESTRUNNER}/recheck/${hash}`, { method: 'POST', cache: 'no-store' });
    if (!res.ok) {
        throw new Error(`/recheck returned ${res.status}`);
    }
}

export async function triggerRecheckByPrId(prId: number): Promise<void> {
    const res = await fetch(`${TESTRUNNER}/recheck/pr/${prId}`, { method: 'POST', cache: 'no-store' });
    if (!res.ok) {
        throw new Error(`/recheck/pr returned ${res.status}`);
    }
}

export async function getRunningHashes(): Promise<string[]> {
    // Values are WorkerJob payloads now, not bare hashes.
    const raw = await getRedis().hvals('test:workers');
    return raw
        .map((v) => {
            try {
                return (JSON.parse(v) as WorkerJob).commit;
            } catch {
                return null;
            }
        })
        .filter((c): c is string => Boolean(c));
}

/** What a single worker replica is doing right now. */
export type WorkerJob = {
    worker: string;
    commit: string;
    task: TaskName;
    stage: string;
    started: number;
};

export type QueuedJob = {
    commit: string;
    task: TaskName;
};

export type SystemStatus = {
    /** Server clock, so elapsed times don't drift with the browser's. */
    now: number;
    workers: WorkerJob[];
    queue: QueuedJob[];
    fastQueue: QueuedJob[];
};

export async function fetchStatus(): Promise<SystemStatus> {
    const res = await fetch(`${TESTRUNNER}/status`, { cache: 'no-store' });
    if (!res.ok) {
        throw new Error(`/status returned ${res.status}`);
    }
    return res.json();
}

export type PoolStatus = {
    ready: number;
    building: number;
};

export async function fetchPoolStatus(): Promise<PoolStatus> {
    const r = getRedis();
    const [ready, building] = await Promise.all([
        r.scard('test:pool:ready'),
        r.scard('test:pool:building'),
    ]);
    return { ready, building };
}

export async function readLog(hash: string, type: 'install' | 'test' | 'init'): Promise<string | null> {
    const filePath = path.join(RESULTS, `${hash}.${type}.log`);
    try {
        return await fs.readFile(filePath, 'utf-8');
    } catch (e: unknown) {
        if ((e as NodeJS.ErrnoException).code === 'ENOENT') {
            return null;
        }
        throw e;
    }
}

export async function readPreCommitLog(hash: string): Promise<string | null> {
    const filePath = path.join(RESULTS, `${hash}.precommit.log`);
    try {
        return await fs.readFile(filePath, 'utf-8');
    } catch (e: unknown) {
        if ((e as NodeJS.ErrnoException).code === 'ENOENT') {
            return null;
        }
        throw e;
    }
}

export async function triggerNotify(hash: string): Promise<void> {
    const res = await fetch(`${TESTRUNNER}/notify/${hash}`, { method: 'POST', cache: 'no-store' });
    if (!res.ok) {
        throw new Error(`/notify returned ${res.status}`);
    }
}

// --- dev sources / db copies / the single Odoo instance ---------------------------

/**
 * Next.js redacts any error *thrown* out of a 'use server' action in production builds
 * (only a generic "Server Components render" message + digest reaches the client — see
 * https://nextjs.org/docs/messages/failed-to-find-server-action's sibling guidance on
 * expected errors). The backend's real `{error}` message would be lost that way, so
 * every mutating action below returns this shape instead of throwing; only the plain
 * `fetchX` queries (used as React Query `queryFn`s, which want a throw) keep throwing.
 */
export type ActionResult<T> = { ok: true; data: T } | { ok: false; error: string };

async function callApi<T>(url: string, init: RequestInit, fallback: string): Promise<ActionResult<T>> {
    try {
        const res = await fetch(url, { cache: 'no-store', ...init });
        if (!res.ok) {
            const body = await res.json().catch(() => ({}));
            return { ok: false, error: body.error ?? fallback };
        }
        return { ok: true, data: await res.json() };
    } catch (e) {
        return { ok: false, error: e instanceof Error ? e.message : fallback };
    }
}

export type Source = {
    id: string;
    baseDb: string;
    ready: boolean;
    resetting: boolean;
};

export async function fetchSources(): Promise<Source[]> {
    const res = await fetch(`${TESTRUNNER}/sources`, { cache: 'no-store' });
    if (!res.ok) {
        throw new Error(`/sources returned ${res.status}`);
    }
    return res.json();
}

export async function resetSource(source: string): Promise<ActionResult<{ resetting: string }>> {
    return callApi(`${TESTRUNNER}/sources/${source}/reset`, { method: 'POST' }, `/sources/${source}/reset failed`);
}

export type CopyStatus = 'creating' | 'ready' | 'failed';

export type Copy = {
    name: string;
    source: string;
    createdAt: number;
    status: CopyStatus;
    error: string | null;
};

export async function fetchCopies(): Promise<Copy[]> {
    const res = await fetch(`${TESTRUNNER}/copies`, { cache: 'no-store' });
    if (!res.ok) {
        throw new Error(`/copies returned ${res.status}`);
    }
    return res.json();
}

export async function createCopy(name: string, source: string): Promise<ActionResult<{ created: string }>> {
    return callApi(
        `${TESTRUNNER}/copies`,
        {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, source }),
        },
        '/copies (create) failed'
    );
}

export async function deleteCopy(name: string): Promise<ActionResult<{ deleted: string }>> {
    return callApi(`${TESTRUNNER}/copies/${name}`, { method: 'DELETE' }, `/copies/${name} (delete) failed`);
}

export type InstanceStatus = {
    status: 'stopped' | 'starting' | 'running' | 'error';
    db: string | null;
    install: string | null;
    upgrade: string | null;
    syncedPr: number | null;
    syncedCommit: string | null;
    /** Relative path under the mounted local codebase root; mutually exclusive with syncedPr. */
    syncedLocal: string | null;
    startedAt: number | null;
    error: string | null;
    url: string | null;
};

export async function fetchInstance(): Promise<InstanceStatus> {
    const res = await fetch(`${TESTRUNNER}/instance`, { cache: 'no-store' });
    if (!res.ok) {
        throw new Error(`/instance returned ${res.status}`);
    }
    return res.json();
}

export async function attachInstance(
    name: string,
    install?: string,
    upgrade?: string
): Promise<ActionResult<InstanceStatus>> {
    return callApi(
        `${TESTRUNNER}/instance/attach`,
        {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, install, upgrade }),
        },
        '/instance/attach failed'
    );
}

export async function restartInstance(
    install?: string,
    upgrade?: string
): Promise<ActionResult<InstanceStatus>> {
    return callApi(
        `${TESTRUNNER}/instance/restart`,
        {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ install, upgrade }),
        },
        '/instance/restart failed'
    );
}

export async function detachInstance(): Promise<ActionResult<InstanceStatus>> {
    return callApi(`${TESTRUNNER}/instance/detach`, { method: 'POST' }, '/instance/detach failed');
}

export async function syncInstance(prId: number): Promise<ActionResult<{ prId: number; commit: string }>> {
    return callApi(
        `${TESTRUNNER}/instance/sync`,
        {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ prId }),
        },
        '/instance/sync failed'
    );
}

export async function fetchLocalAddonsFolders(): Promise<string[]> {
    const res = await fetch(`${TESTRUNNER}/instance/local-addons`, { cache: 'no-store' });
    if (!res.ok) {
        throw new Error(`/instance/local-addons returned ${res.status}`);
    }
    const body = await res.json();
    return body.folders;
}

export async function syncLocalInstance(path: string): Promise<ActionResult<{ path: string }>> {
    return callApi(
        `${TESTRUNNER}/instance/sync-local`,
        {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ path }),
        },
        '/instance/sync-local failed'
    );
}

export async function fetchInstanceLog(): Promise<{ log: string }> {
    const res = await fetch(`${TESTRUNNER}/instance/log`, { cache: 'no-store' });
    if (!res.ok) {
        throw new Error(`/instance/log returned ${res.status}`);
    }
    return res.json();
}

export async function fetchSuggestedUpgrades(): Promise<ActionResult<{ modules: string[] }>> {
    return callApi(`${TESTRUNNER}/instance/suggested-upgrades`, {}, '/instance/suggested-upgrades failed');
}
