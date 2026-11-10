import { validatePlan } from './validator.js';
export function prepare(raw) {
  const result = validatePlan(raw);
  if (!result.ok) return { exit: 2, errors: result.errors };
  return { exit: 0, plan: result.value };
}
