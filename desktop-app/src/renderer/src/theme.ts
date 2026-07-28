'use client'

import { Container, createTheme, getSize } from '@mantine/core'

export const theme = createTheme({
  components: {
    // Mantine's default xl container (1320px) wastes space on wide desktop
    // monitors — widen just that breakpoint, leave xs/sm/md/lg untouched.
    Container: Container.extend({
      vars: (_theme, { size, fluid }) => ({
        root: {
          '--container-size': fluid
            ? undefined
            : size === 'xl'
              ? '1600px'
              : getSize(size, 'container-size')
        }
      })
    })
  }
})
