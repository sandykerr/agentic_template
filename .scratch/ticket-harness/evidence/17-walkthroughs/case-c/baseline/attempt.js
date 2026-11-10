export class Attempt {
  constructor() { this.status = 'starting'; this.events = ['starting']; }
  submit() { this.status = 'submitted'; this.events.push('submitted'); }
  complete() { this.status = 'complete'; this.events.push('complete'); }
}
