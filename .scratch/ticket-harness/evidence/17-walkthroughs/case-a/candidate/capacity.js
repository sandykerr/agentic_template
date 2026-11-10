export class Capacity {
  constructor(limit) { this.remaining = limit; }
  reserve(units) {
    if (!Number.isInteger(units) || units <= 0 || units > this.remaining) return false;
    this.remaining -= units;
    return true;
  }
  cancel(units) {
    if (!Number.isInteger(units) || units <= 0) return false;
    this.remaining += units;
    return true;
  }
}
