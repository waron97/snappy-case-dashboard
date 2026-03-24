'use client';

import { useState, useTransition } from 'react';
import { IconSettings } from '@tabler/icons-react';
import { ActionIcon, Button, Modal, PasswordInput, Stack, TextInput } from '@mantine/core';
import { saveCredentials } from '../../app/credentials';
import type { Credentials } from '../../app/credentials-reader';

type Props = {
    currentValues: Credentials | null;
};

export default function CredentialsModal({ currentValues }: Props) {
    const [opened, setOpened] = useState(false);
    const [isPending, startTransition] = useTransition();

    const [formData, setFormData] = useState<Credentials>(
        currentValues || {
            cred_odoo_api_key: '',
            cred_odoo_uid: '',
        }
    );

    const handleSubmit = () => {
        startTransition(async () => {
            await saveCredentials(formData);
        });
    };

    return (
        <>
            <ActionIcon variant="subtle" size="lg" color="gray" onClick={() => setOpened(true)}>
                <IconSettings size={20} />
            </ActionIcon>

            <Modal
                opened={opened}
                onClose={() => setOpened(false)}
                title="Configure Credentials"
                centered
            >
                <Stack gap="md">
                    <TextInput
                        label="Odoo UID"
                        placeholder="2"
                        value={formData.cred_odoo_uid}
                        onChange={(e) =>
                            setFormData({ ...formData, cred_odoo_uid: e.currentTarget.value })
                        }
                        disabled={isPending}
                    />
                    <PasswordInput
                        label="Odoo API Key"
                        placeholder="api_key"
                        value={formData.cred_odoo_api_key}
                        onChange={(e) =>
                            setFormData({ ...formData, cred_odoo_api_key: e.currentTarget.value })
                        }
                        disabled={isPending}
                    />

                    <Button onClick={handleSubmit} loading={isPending} fullWidth>
                        Save Credentials
                    </Button>
                </Stack>
            </Modal>
        </>
    );
}
