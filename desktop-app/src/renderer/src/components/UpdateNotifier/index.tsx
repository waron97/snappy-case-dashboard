import { useEffect } from 'react'
import { toast } from 'react-toastify'
import { Button, Stack, Text } from '@mantine/core'

function UpdateToast(): React.JSX.Element {
  return (
    <Stack gap="xs">
      <Text size="sm">An update has been downloaded.</Text>
      <Button size="xs" onClick={() => window.api.updater.quitAndInstall()}>
        Restart & update
      </Button>
    </Stack>
  )
}

export default function UpdateNotifier(): null {
  useEffect(() => {
    return window.api.updater.onUpdateDownloaded(() => {
      toast(<UpdateToast />, { autoClose: false, closeOnClick: false })
    })
  }, [])

  return null
}
