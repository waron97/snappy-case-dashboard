import { cookies } from 'next/headers';

export interface Credentials {
    cred_odoo_api_key: string;
    cred_odoo_uid: string;
}

export async function getCredentials(): Promise<Credentials | null> {
    const perUserAuth = process.env.ENABLE_PER_USER_AUTH !== '0';

    if (!perUserAuth) {
        const uid = process.env.ODOO_UID;
        const apiKey = process.env.ODOO_API_KEY;
        if (!uid || !apiKey) return null;
        return { cred_odoo_uid: uid, cred_odoo_api_key: apiKey };
    }

    const cookieStore = await cookies();

    const cred_odoo_api_key = cookieStore.get('cred_odoo_api_key')?.value;
    const cred_odoo_uid = cookieStore.get('cred_odoo_uid')?.value;

    if (!cred_odoo_api_key || !cred_odoo_uid) {
        return null;
    }

    return {
        cred_odoo_api_key,
        cred_odoo_uid,
    };
}
