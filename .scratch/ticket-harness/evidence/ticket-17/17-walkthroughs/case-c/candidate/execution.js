import { summary } from './report.js';
export function runTicket(a) {
  a.submit();
  a.status = 'complete';
  return summary(a);
}
