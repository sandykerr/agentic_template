from dataclasses import dataclass

@dataclass(frozen=True)
class Ticket:
    id: str
    dependencies: tuple[str, ...]

def parse(text):
    tickets = []
    for entry in text.split(","):
        identity, sep, rest = entry.partition(":")
        identity = identity.strip()
        if not identity or not sep:
            raise ValueError("expected id:dependencies")
        dependencies = tuple(d.strip() for d in rest.split("+") if d.strip())
        tickets.append(Ticket(identity, dependencies))
    by_id = {t.id: t for t in tickets}
    if len(by_id) != len(tickets):
        raise ValueError("duplicate ID")
    visiting, done = set(), set()
    def visit(identity):
        if identity not in by_id:
            raise ValueError("unknown dependency")
        if identity in visiting:
            raise ValueError("cycle")
        if identity in done:
            return
        visiting.add(identity)
        for dependency in by_id[identity].dependencies:
            visit(dependency)
        visiting.remove(identity)
        done.add(identity)
    for ticket in tickets:
        visit(ticket.id)
    return tuple(tickets)
