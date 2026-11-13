# Python environment

Use [environment.yml](../../environment.yml). Put project dependencies in
[pyproject.toml](../../pyproject.toml), shared development tools in environment.yml.
The [testing policy](testing.md#check-commands) owns project check/tool setup.

From the checkout being developed:

```bash
export XDG_CACHE_HOME=/home/ajkerr1/development/agentic_template/.micromamba/cache
micromamba run --prefix /home/ajkerr1/development/agentic_template/.micromamba/envs/dev python -m pytest
```

Set the cache in every shell using `micromamba run`: process locks need a writable
cache and the sandbox's default home cache may be read-only. The prefix's absolute
`bin/python` also works without micromamba or this setting. Use that interpreter
for `-m pip` and `-m pytest`.

Reuse this absolute prefix across worktrees and agents; run commands from the
checkout being developed using its source or documented import configuration.
Coordinate shared package changes. An editable install points at one checkout;
use a separate worktree environment for an isolated install or different versions.

From a new clone or isolated worktree root, create its environment:

```bash
micromamba --no-rc --root-prefix "$PWD/.micromamba" create --yes --prefix "$PWD/.micromamba/envs/dev" --file environment.yml
```

After changing environment.yml, update the existing environment with:

```bash
micromamba --no-rc --root-prefix "$PWD/.micromamba" install --yes --prefix "$PWD/.micromamba/envs/dev" --file environment.yml
```

Use that clone/worktree's absolute prefix and writable cache afterward.
