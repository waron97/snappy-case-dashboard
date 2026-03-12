import { ReactNode } from 'react';
import { Box, Paper, Stack, Text } from '@mantine/core';

type Props = {
  title?: string;
  children?: ReactNode;
};

export default function UiCard({ title, children }: Props) {
  // -------------------------------------
  // Hooks
  // -------------------------------------

  // -------------------------------------
  // Queries
  // -------------------------------------

  // -------------------------------------
  // Effects
  // -------------------------------------

  // -------------------------------------
  // Functions
  // -------------------------------------

  // -------------------------------------
  // Local Variables
  // -------------------------------------

  // -------------------------------------

  return (
    <Paper withBorder radius={4} p="xs" component="section">
      <Stack gap="md">
        <Text size="lg" c="cyan">
          {title}
        </Text>
        <Box>{children}</Box>
      </Stack>
    </Paper>
  );
}
