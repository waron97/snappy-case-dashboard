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

export type PrRecord = {
    id: number;
    title: string;
    author: string;
    sourceBranch: string;
    commitId: string;
    status: PrStatus;
    preCommitStatus: PreCommitStatus | null;
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
    return getRedis().hvals('test:workers');
}

export async function readLog(hash: string, type: 'install' | 'test'): Promise<string | null> {
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
