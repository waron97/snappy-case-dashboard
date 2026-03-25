import '@mantine/core/styles.css';
import '@mantine/dates/styles.css';
import '@xyflow/react/dist/style.css';

import { Metadata } from 'next';
import { JetBrains_Mono } from 'next/font/google';
import {
    Box,
    ColorSchemeScript,
    Container,
    Group,
    mantineHtmlProps,
    MantineProvider,
    Title,
} from '@mantine/core';
import CredentialsModal from '@/components/CredentialsModal';
import HeaderNav from '@/components/HeaderNav';
import OdooNavigateModal from '@/components/OdooNavigateModal';
import { QueryProvider } from '@/components/QueryProvider';
import { theme } from '../theme';
import { getCredentials } from './credentials-reader';

const jetbrainsMono = JetBrains_Mono({ subsets: ['latin'] });

const db = process.env.ODOO_DB;
const prefix = db === 'sorgenia-test-02' ? '[T02] ' : db === 'sorgenia-test-01' ? '[T01] ' : '';

export const metadata: Metadata = {
    title: {
        template: `${prefix}%s`,
        default: `${prefix}Snappy`,
    },
    description: 'Case management dashboard',
};

export default async function RootLayout({ children }: { children: any }) {
    const credentials = await getCredentials();

    return (
        <html lang="en" {...mantineHtmlProps} className={jetbrainsMono.className}>
            <head>
                <ColorSchemeScript />
                <link rel="shortcut icon" href="/favicon.svg" />
                <meta
                    name="viewport"
                    content="minimum-scale=1, initial-scale=1, width=device-width, user-scalable=no"
                />
            </head>
            <body>
                <MantineProvider theme={theme} defaultColorScheme="dark">
                    <QueryProvider>
                        <Box
                            py="md"
                            style={{
                                borderBottom: '1px solid var(--mantine-color-gray-8)',
                                position: 'relative',
                                zIndex: 200,
                            }}
                        >
                            <header>
                                <Container size="xl">
                                    <div
                                        style={{
                                            display: 'grid',
                                            gridTemplateColumns: '1fr auto 1fr',
                                            alignItems: 'center',
                                        }}
                                    >
                                        <Group>
                                            <a href="/">
                                                <img
                                                    src="/logo.svg"
                                                    alt="Snappy"
                                                    style={{ height: 60 }}
                                                />
                                            </a>
                                        </Group>
                                        <HeaderNav />
                                        <Group justify="flex-end">
                                            <CredentialsModal currentValues={credentials} />
                                        </Group>
                                    </div>
                                </Container>
                            </header>
                        </Box>
                        {credentials === null && (
                            <Box
                                style={{
                                    position: 'fixed',
                                    inset: 0,
                                    zIndex: 100,
                                    backgroundColor: 'rgba(0, 0, 0, 0.75)',
                                    display: 'flex',
                                    alignItems: 'center',
                                    justifyContent: 'center',
                                    flexDirection: 'column',
                                    gap: '1rem',
                                }}
                            >
                                <Title order={2} c="white">
                                    Please Configure Your Credentials
                                </Title>
                                <Title order={4} c="dimmed">
                                    Click the settings icon (⚙️) in the top right to configure your
                                    Odoo credentials.
                                </Title>
                            </Box>
                        )}
                        <OdooNavigateModal />
                        {credentials !== null && children}
                    </QueryProvider>
                </MantineProvider>
            </body>
        </html>
    );
}
