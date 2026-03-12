import { ReactNode } from 'react';
import { Box, Group, Paper, Stack, Text } from '@mantine/core';

type Props = {
  title?: string;
  rightElement?: ReactNode;
  children?: ReactNode;
};

export default function UiCard({ title, children, rightElement }: Props) {
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
        <Group gap="md" justify="space-between">
          <Text size="lg" c="cyan">
            {title}
          </Text>
          <Box>{rightElement}</Box>
        </Group>
        <Box>{children}</Box>
      </Stack>
    </Paper>
  );
}
