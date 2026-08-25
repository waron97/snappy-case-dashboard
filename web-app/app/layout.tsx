import '@mantine/core/styles.css';

import { Metadata } from 'next';
import { JetBrains_Mono } from 'next/font/google';
import { Box, ColorSchemeScript, Container, Group, mantineHtmlProps, MantineProvider } from '@mantine/core';
import HeaderNav from '@/components/HeaderNav';
import { QueryProvider } from '@/components/QueryProvider';
import { theme } from '../theme';

const jetbrainsMono = JetBrains_Mono({ subsets: ['latin'] });

export const metadata: Metadata = {
    title: {
        template: '%s',
        default: 'Snappy',
    },
    description: 'Test-runner control panel',
};

export default function RootLayout({ children }: { children: any }) {
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
                                        <Group justify="flex-end" />
                                    </div>
                                </Container>
                            </header>
                        </Box>
                        {children}
                    </QueryProvider>
                </MantineProvider>
            </body>
        </html>
    );
}
