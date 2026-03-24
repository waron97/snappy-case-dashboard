'use server';

import { cookies } from 'next/headers';
import { redirect } from 'next/navigation';
import type { Credentials } from './credentials-reader';

export async function saveCredentials(creds: Credentials): Promise<void> {
    const cookieStore = await cookies();

    const isProduction = process.env.NODE_ENV === 'production';

    const cookieOptions = {
        httpOnly: true,
        sameSite: 'lax' as const,
        path: '/',
        maxAge: 365 * 24 * 60 * 60, // 1 year in seconds
        secure: isProduction,
    };

    cookieStore.set('cred_odoo_api_key', creds.cred_odoo_api_key, cookieOptions);
    cookieStore.set('cred_odoo_uid', creds.cred_odoo_uid, cookieOptions);

    redirect('/');
}
