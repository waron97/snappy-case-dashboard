import '@mantine/core/styles.css';
import '@mantine/dates/styles.css';

import { Metadata } from 'next';
import {
  Box,
  ColorSchemeScript,
  Container,
  mantineHtmlProps,
  MantineProvider,
  Title,
} from '@mantine/core';
import { QueryProvider } from '@/components/QueryProvider';
import { theme } from '../theme';

export const metadata: Metadata = {
  title: 'Snappy Case',
  description: 'Case management dashboard',
};

export default function RootLayout({ children }: { children: any }) {
  return (
    <html lang="en" {...mantineHtmlProps}>
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
            <Box py="md" style={{ borderBottom: '1px solid var(--mantine-color-gray-8)' }}>
              <header>
                <Container size="xl">
                  <a href="/">
                    <Title fz={21}>Snappy Case</Title>
                  </a>
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
