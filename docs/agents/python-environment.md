# Python development environment

Use the micromamba environment defined in [`environment.yml`](../../environment.yml) for Python development. It supplies Python 3.12, pip, and pytest. Project dependencies belong in the project's packaging metadata when that exists; add shared development tools to `environment.yml`.

## Use the existing environment

On this machine the environment prefix is:

```text
/home/ajkerr1/development/agentic_template/.micromamba/envs/dev
```

From the checkout being developed, run commands without shell activation:

```bash
export XDG_CACHE_HOME=/home/ajkerr1/development/agentic_template/.micromamba/cache
micromamba run --prefix /home/ajkerr1/development/agentic_template/.micromamba/envs/dev python --version
micromamba run --prefix /home/ajkerr1/development/agentic_template/.micromamba/envs/dev python -m pip --version
micromamba run --prefix /home/ajkerr1/development/agentic_template/.micromamba/envs/dev python -m pytest
```

Set `XDG_CACHE_HOME` in each new agent shell that uses `micromamba run`: micromamba writes process locks there, and the default home-directory cache may be read-only in the sandbox. This setting keeps those writes inside the checkout. For a simple Python invocation, the environment's absolute `bin/python` path also works without `micromamba run` or this cache setting.

Use `python -m pip` and `python -m pytest` through this environment so each tool uses its interpreter. Run the repository's documented checks once implementation provides them; the setup itself does not add a test suite.

## Create or update an environment

For a new clone, run from its repository root:

```bash
micromamba --no-rc --root-prefix "$PWD/.micromamba" create --yes --prefix "$PWD/.micromamba/envs/dev" --file environment.yml
```

For an existing environment after changing `environment.yml`:

```bash
micromamba --no-rc --root-prefix "$PWD/.micromamba" install --yes --prefix "$PWD/.micromamba/envs/dev" --file environment.yml
```

The repository-local root keeps the environment and package cache in the ignored `.micromamba/` directory. Creation and package changes require network access to conda-forge. The environment file constrains the Python minor version; it is not an exact package lockfile. Use the new clone's absolute prefix and cache path in subsequent commands.

## Worktrees and agents

Agents and worktrees on this machine can reuse the existing absolute prefix above. Relative `.micromamba/` paths refer to the current checkout, so they will not find the original environment from a separate worktree. Keep the working directory in the checkout being developed when invoking Python or tests.

For worktree-local imports, use that checkout's source or the project's documented test configuration. An editable installation in the shared environment points at one checkout; when an editable install or different dependency versions are needed for isolated work, create a separate environment in that worktree using the creation command above. Reuse the shared environment for execution; coordinate package changes across agents.
