import os
from pathlib import Path
import subprocess
import tempfile

def atomic_write(destination, text):
    destination = Path(destination)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8",
                                         dir=destination.parent, delete=False) as file:
            temporary = Path(file.name)
            file.write(text)
        os.replace(temporary, destination)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)

def invoke(argv, cwd, timeout):
    return subprocess.run(argv, cwd=cwd, capture_output=True, text=True,
                          timeout=timeout, check=False)
