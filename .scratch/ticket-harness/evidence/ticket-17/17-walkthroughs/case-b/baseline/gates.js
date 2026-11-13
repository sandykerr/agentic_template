export class Gates {
  constructor(records = []) { this.records = records; }
  record(id, source) {
    const gate = { id, source, valid: true };
    this.records.push(gate);
    return gate;
  }
  invalidate(source) {
    for (const gate of this.records) if (gate.source !== source) gate.valid = false;
  }
}
