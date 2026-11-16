# Python environment

Use the current checkout's uv-managed `.venv` by default for Python, dependency
installation, and checks. Run commands from that checkout's root and use
`.venv/bin/python` explicitly so shell activation is unnecessary.

## Setup and synchronization

For a new clone or worktree, create and populate its environment:

```bash
export UV_CACHE_DIR="$PWD/.uv-cache"
uv venv --python 3.12 .venv
uv pip sync --python .venv/bin/python requirements-uv.txt
```

Reuse an existing `.venv`; run the sync command after the frozen requirements
change. Set `UV_CACHE_DIR` in each shell using uv so its cache is writable.
Each worktree owns its environment and editable project install. Create a fresh
environment in a new worktree rather than sharing another checkout's `.venv`.

## Dependencies and checks

[requirements-uv.txt](../../requirements-uv.txt) freezes the environment,
including the editable project and its `dev` extra. Put project dependencies and
pinned project check tools in [pyproject.toml](../../pyproject.toml), and shared
development tools in [environment.yml](../../environment.yml). Keep the PyPI
equivalents in [requirements-uv.in](../../requirements-uv.in) aligned with
environment.yml. Follow the [README refresh instructions](../../README.md#python-setup-with-uv)
to regenerate and sync the frozen requirements after dependency changes.

Use `.venv/bin/python -m pip` if pip is specifically needed. Use the
[testing policy's check commands](testing.md#check-commands) for verification.
Micromamba remains an optional alternative when explicitly requested; uv is the
default for agent work.
