import dayjs from 'dayjs'
import { getAssets, odooRead, OneToMany } from '@/lib/odoo-api'
import { useQuery } from '@tanstack/react-query'
import { Badge, Divider, Grid, Group, Stack, Table, Tabs, Text } from '@mantine/core'

type Props = {
  id: number
}

type PartnerFields = {
  type: 'contact' | 'invoice' | 'delivery' | 'other'
  is_company: boolean
  company_type: string
  business_type: string | false
  category: string | false
  user_sequence: string | false
  fiscal_code: string | false
  vat: string | false
  email: string | false
  phone: string | false
  mobile: string | false
  pec_email: string | false
  pa_pec_email: string | false
  // Address
  toponym_id: OneToMany | false
  street: string | false
  street_num: string | false
  street2: string | false
  apartment_number: string | false
  floor: string | false
  stairs: string | false
  zip_id: OneToMany | false
  city_id: OneToMany | false
  zip: string | false
  city: string | false
  state_id: OneToMany | false
  country_id: OneToMany | false
  parent_id: OneToMany | false
  // Personal
  birth_date: string | false
  gender: 'f' | 'm' | false
  // Company
  sdi_code: string | false
  // Status
  customer_care_category: string | false
  total_client_status: string | false
  credit_status: OneToMany | false
}

const rel = (field: OneToMany | false): string | false =>
  field ? `${field[1]} (#${field[0]})` : false

export default function ResPartner(props: Props) {
  const { id } = props

  const { data: assets } = useQuery({
    queryKey: ['res.partner', id, 'assets'],
    queryFn: () => getAssets({ type: 'product', accountcode: String(id) })
  })

  const { data } = useQuery<PartnerFields>({
    queryKey: ['res.partner', id, 'popover'],
    queryFn: () =>
      odooRead(
        'res.partner',
        [id],
        [
          'type',
          'is_company',
          'company_type',
          'business_type',
          'category',
          'user_sequence',
          'fiscal_code',
          'vat',
          'email',
          'phone',
          'mobile',
          'pec_email',
          'pa_pec_email',
          'toponym_id',
          'street',
          'street_num',
          'street2',
          'apartment_number',
          'floor',
          'stairs',
          'zip_id',
          'city_id',
          'zip',
          'city',
          'state_id',
          'country_id',
          'parent_id',
          'birth_date',
          'gender',
          'customer_care_category',
          'total_client_status',
          'credit_status',
          'sdi_code'
        ]
      ).then((res) => res[0])
  })

  const item = (label: string, value: string | number) => (
    <Stack gap={0}>
      <Text c="dimmed" size="sm">
        {label}
      </Text>
      <Text fw="bold">{value}</Text>
    </Stack>
  )

  if (!data) {
    return null
  }

  const renderAssets = () => {
    if (!assets) {
      return null
    }

    return (
      <Table>
        <Table.Thead>
          <Table.Tr>
            <Table.Td>ID</Table.Td>
            <Table.Td>State</Table.Td>
            <Table.Td>SM State</Table.Td>
            <Table.Td>Create date</Table.Td>
          </Table.Tr>
        </Table.Thead>
        <Table.Tbody>
          {assets.map((asset) => (
            <Table.Tr key={asset._id}>
              <Table.Td>{asset._id}</Table.Td>
              <Table.Td>{asset.assetstatus}</Table.Td>
              <Table.Td>{asset.sm_state}</Table.Td>
              <Table.Td>{dayjs(asset.createdate).format('D/M/YY HH:mm')}</Table.Td>
            </Table.Tr>
          ))}
        </Table.Tbody>
      </Table>
    )
  }

  const isContact = data.type === 'contact' || !data.type

  const streetLine = [data.street, data.street_num].filter(Boolean).join(' ') || false

  const cityLine = [data.zip, data.city].filter(Boolean).join(' ') || false

  const hasAddress =
    data.toponym_id ||
    streetLine ||
    data.street2 ||
    data.apartment_number ||
    data.floor ||
    data.stairs ||
    data.zip_id ||
    data.city_id ||
    cityLine ||
    data.state_id ||
    data.country_id

  const hasStatus = data.customer_care_category || data.total_client_status || data.credit_status

  return (
    <Stack gap="xs">
      <Group gap={4}>
        <Badge variant="light">
          {data.company_type || (data.is_company ? 'Company' : data.type)}
        </Badge>
        {data.category && (
          <Badge variant="outline" color="gray">
            {data.category}
          </Badge>
        )}
      </Group>

      <Tabs defaultValue="base">
        <Tabs.List>
          <Tabs.Tab value="base">Base information</Tabs.Tab>
          <Tabs.Tab value="assets">Assets</Tabs.Tab>
        </Tabs.List>

        <Tabs.Panel value="base">
          <Stack gap="sm" pt="sm">
            {/* Identity */}
            {data.user_sequence && item('Sequence', data.user_sequence)}
            {data.fiscal_code && item('Fiscal code', data.fiscal_code)}
            {!data.is_company && data.vat && item('VAT', data.vat)}

            {/* Contact info */}
            {isContact &&
              (data.email || data.phone || data.mobile || data.pec_email || data.pa_pec_email) && (
                <>
                  <Divider />
                  <Grid>
                    <Grid.Col span={6}>
                      <Stack gap="sm">
                        {data.email && item('Email', data.email)}
                        {data.pec_email && item('PEC', data.pec_email)}
                        {data.pa_pec_email && item('PA PEC', data.pa_pec_email)}
                      </Stack>
                    </Grid.Col>
                    <Grid.Col span={6}>
                      <Stack gap="sm">
                        {data.phone && item('Phone', data.phone)}
                        {data.mobile && item('Mobile', data.mobile)}
                      </Stack>
                    </Grid.Col>
                  </Grid>
                </>
              )}

            {/* Address */}
            {hasAddress && (
              <>
                <Divider />
                <Grid>
                  <Grid.Col span={6}>
                    <Stack gap="sm">
                      {data.toponym_id && item('Toponym', rel(data.toponym_id) as string)}
                      {streetLine && item('Street', streetLine)}
                      {data.street2 && item('Street 2', data.street2)}
                      {data.apartment_number && item('Apartment', data.apartment_number)}
                      {data.floor && item('Floor', data.floor)}
                      {data.stairs && item('Stairs', data.stairs)}
                    </Stack>
                  </Grid.Col>
                  <Grid.Col span={6}>
                    <Stack gap="sm">
                      {data.zip_id
                        ? item('ZIP', rel(data.zip_id) as string)
                        : cityLine && item('ZIP', data.zip || '')}
                      {data.city_id
                        ? item('City', rel(data.city_id) as string)
                        : data.city && item('City', data.city)}
                      {data.state_id && item('Province', rel(data.state_id) as string)}
                      {data.country_id && item('Country', rel(data.country_id) as string)}
                      {data.parent_id && item('Company', rel(data.parent_id) as string)}
                    </Stack>
                  </Grid.Col>
                </Grid>
              </>
            )}

            {/* Company info */}
            {data.is_company && (data.vat || data.business_type || data.sdi_code) && (
              <>
                <Divider />
                <Grid>
                  <Grid.Col span={6}>
                    <Stack gap="sm">
                      {data.vat && item('VAT', data.vat)}
                      {data.business_type && item('Business type', data.business_type)}
                    </Stack>
                  </Grid.Col>
                  <Grid.Col span={6}>
                    <Stack gap="sm">{data.sdi_code && item('SDI code', data.sdi_code)}</Stack>
                  </Grid.Col>
                </Grid>
              </>
            )}

            {/* Personal info */}
            {!data.is_company && isContact && (data.birth_date || data.gender) && (
              <>
                <Divider />
                <Grid>
                  <Grid.Col span={6}>
                    <Stack gap="sm">
                      {data.birth_date &&
                        item('Birth date', dayjs(data.birth_date).format('D/M/YYYY'))}
                    </Stack>
                  </Grid.Col>
                  <Grid.Col span={6}>
                    <Stack gap="sm">
                      {data.gender && item('Gender', data.gender === 'f' ? 'Female' : 'Male')}
                    </Stack>
                  </Grid.Col>
                </Grid>
              </>
            )}

            {/* Status */}
            {hasStatus && (
              <>
                <Divider />
                <Stack gap="sm">
                  {data.customer_care_category &&
                    item('Care category', data.customer_care_category)}
                  {data.total_client_status && item('Client status', data.total_client_status)}
                  {data.credit_status && item('Credit status', rel(data.credit_status) as string)}
                </Stack>
              </>
            )}
          </Stack>
        </Tabs.Panel>

        <Tabs.Panel value="assets">{renderAssets()}</Tabs.Panel>
      </Tabs>
    </Stack>
  )
}
