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
        dependencies = tuple(d.strip() for d in rest.split("+")) if rest.strip() else ()
        if any(not dependency for dependency in dependencies):
            raise ValueError("empty dependency ID")
        tickets.append(Ticket(identity, dependencies))
    by_id = {t.id: t for t in tickets}
    if len(by_id) != len(tickets):
        raise ValueError("duplicate ID")
    visiting, done = set(), set()
    for ticket in tickets:
        stack = [(ticket.id, False)]
        while stack:
            identity, leaving = stack.pop()
            if leaving:
                visiting.remove(identity)
                done.add(identity)
                continue
            if identity not in by_id:
                raise ValueError("unknown dependency")
            if identity in visiting:
                raise ValueError("cycle")
            if identity in done:
                continue
            visiting.add(identity)
            stack.append((identity, True))
            stack.extend((dependency, False)
                         for dependency in reversed(by_id[identity].dependencies))
    return tuple(tickets)
