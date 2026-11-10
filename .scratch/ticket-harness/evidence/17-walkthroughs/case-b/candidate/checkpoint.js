import { Gates } from './gates.js';
export function save(gates, verified) {
  return { gates: gates.records, verifiedIds: verified.map(g => g.id) };
}
export function restore(checkpoint) {
  const gates = new Gates(checkpoint.gates.map(g => ({ ...g })));
  const verified = checkpoint.verifiedIds.map(id => ({ ...gates.records.find(g => g.id === id) }));
  return { gates, verified };
}
export function ready(verified) { return verified.every(g => g.valid); }
