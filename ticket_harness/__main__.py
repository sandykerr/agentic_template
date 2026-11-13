"""Public run/status CLI; JSON output is also the inspectable record contract."""

import argparse
import json
import sys
from pathlib import Path

from ticket_harness import qa
from ticket_harness.records import GateFailure
from ticket_harness.runner import continue_run, run


def main() -> int:
    """Dispatch run/status/stop/continue from process arguments and return an exit code.

    Print the resulting record as JSON on stdout. Operational/input failures print
    a diagnostic on stderr and return 1; argparse handles invalid CLI arguments.
    Status reads existing state; other operations can write run or repository state.
    """
    parser = argparse.ArgumentParser(prog="ticket-harness")
    operations = parser.add_subparsers(dest="operation", required=True)
    start = operations.add_parser("run")
    start.add_argument("--config", type=Path, required=True)
    start.add_argument("--output", type=Path, required=True)
    status = operations.add_parser("status")
    status.add_argument("run", type=Path)
    for operation in ("stop", "continue"):
        command = operations.add_parser(operation)
        command.add_argument("run", type=Path)
    args = parser.parse_args()
    try:
        if args.operation == "status":
            record = json.loads((args.run / "run.json").read_text())
            code = 0
        elif args.operation == "continue":
            record, code = continue_run(args.run.resolve())
        elif args.operation == "stop":
            record, code = qa.stop(args.run.resolve()), 0
        else:
            record, code = run(args.config.resolve(), args.output.resolve())
        print(json.dumps(record, indent=2))
        return code
    except (GateFailure, OSError, ValueError, KeyError, TypeError) as error:
        print(str(error), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
