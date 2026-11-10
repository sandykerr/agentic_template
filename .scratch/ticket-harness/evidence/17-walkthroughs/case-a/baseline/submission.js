export function submit(capacity, job) {
  if (!capacity.reserve(job.units)) return { accepted: false };
  return { accepted: true, job };
}
export function submitUrgent(capacity, job) {
  capacity.remaining -= job.units;
  return { accepted: true, job };
}
