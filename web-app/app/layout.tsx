import '@mantine/core/styles.css';

import { Metadata } from 'next';
import { ColorSchemeScript, mantineHtmlProps, MantineProvider, Title, Container, Box } from '@mantine/core';
import { theme } from '../theme';
import { QueryProvider } from '../components/QueryProvider';

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
            <Box component="header" py="md" px="lg" style={{ borderBottom: '1px solid var(--mantine-color-gray-8)' }}>
              <Container>
                <Title order={1} size="h3">Snappy Case</Title>
              </Container>
            </Box>
            {children}
          </QueryProvider>
        </MantineProvider>
      </body>
    </html>
  );
}
