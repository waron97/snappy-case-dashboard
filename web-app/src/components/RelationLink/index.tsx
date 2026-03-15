import { useQuery } from '@tanstack/react-query';
import { Anchor, Popover } from '@mantine/core';
import { odooNameGet } from '../../../app/api';
import RelationDropdownBase from './RelationDropdown/base';

type Props = {
  name?: string;
  model: string;
  pgId: number;
  href?: string;
  autoName?: boolean;
};

const hrefMap = (model: string, id: number): string | undefined => {
  const map: { [key: string]: (id: number) => string } = {
    'helpdesk.ticket': (id: number) => `/helpdesk.ticket/${id}`,
  };

  if (map[model]) {
    return map[model](id);
  }
};

export default function RelationLink(props: Props) {
  const { name, model, pgId, href, autoName } = props;

  // -------------------------------------
  // Hooks
  // -------------------------------------

  const { data: odooName } = useQuery({
    queryKey: [model, pgId, 'name'],
    enabled: !!autoName,
    queryFn: () => odooNameGet(model, [pgId]).then((res) => res[0][1]),
  });

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

  const computedName = odooName || name || `${model} #${pgId}`;

  // -------------------------------------

  return (
    <Popover width={600}>
      <Popover.Target>
        <Anchor>{computedName}</Anchor>
      </Popover.Target>
      <Popover.Dropdown>
        <RelationDropdownBase
          name={computedName}
          pgId={pgId}
          model={model}
          href={href || hrefMap(model, pgId)}
        />
      </Popover.Dropdown>
    </Popover>
  );
}
