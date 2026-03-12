import { OdooDomain } from '../../app/api';

export function constructOdooDomain(
  filters: Record<
    string,
    {
      operator: 'ilike' | 'in' | '=' | 'not in' | 'not ilike' | '!=';
      value: string | number | boolean | string[] | number[] | null | undefined;
    }
  >
): OdooDomain {
  const domain: OdooDomain = [];

  for (const [fieldName, { operator, value }] of Object.entries(filters)) {
    // Skip if value is empty string, null, or undefined (but not 0)
    if (value === '' || value === null || value === undefined) {
      continue;
    }

    // Skip if value is an empty array
    if (Array.isArray(value) && value.length === 0) {
      continue;
    }

    // Handle list values with ilike/not ilike specially (OR conditions)
    if (Array.isArray(value) && (operator === 'ilike' || operator === 'not ilike')) {
      const conditions = value.map((v) => [fieldName, operator, v] as OdooDomain);

      if (conditions.length === 1) {
        domain.push(conditions[0]);
      } else if (conditions.length > 1) {
        // Build nested OR structure: ['|', ['|', cond1, cond2], cond3]
        let orStructure: any = conditions[0];
        for (let i = 1; i < conditions.length; i++) {
          orStructure = ['|', orStructure, conditions[i]];
        }
        domain.push(orStructure);
      }
      continue;
    }

    // Handle other cases
    let actualOperator = operator;
    const actualValue: string | number | boolean | string[] | number[] = value;

    // If value is a list and operator is "=" or "!=", convert to "in" or "not in"
    if (Array.isArray(value)) {
      if (operator === '=') {
        actualOperator = 'in';
      } else if (operator === '!=') {
        actualOperator = 'not in';
      }
    }

    domain.push([fieldName, actualOperator, actualValue] as OdooDomain);
  }

  return domain;
}
