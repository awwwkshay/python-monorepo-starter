# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Package Manager

This project uses [uv](https://github.com/astral-sh/uv) exclusively. Do not use `pip`, `poetry`, or other package managers.

```bash
uv sync                  # Install all workspace dependencies
uv add <package>         # Add a dependency
uv add --dev <package>   # Add a dev dependency
```

## Common Commands

```bash
# Run the FastAPI app (from repo root or apps/api/)
uv run fastapi dev apps/api/main.py

# Lint and format
uv run ruff check .
uv run ruff format .

# Type check
uv run ty check

# Run the core CLI
uv run core
```

## Architecture

This is a UV workspace monorepo with two members:

- **`apps/api`** — FastAPI web application. Depends on the `core` package. Entry point is `apps/api/main.py`.
- **`packages/core`** — Shared utility library (src layout: `packages/core/src/core/`). No external dependencies.

The workspace is configured in the root `pyproject.toml` with `[tool.uv.workspace]` globs over `apps/*` and `packages/*`. The `core` package is resolved as a local path dependency via `[tool.uv.sources]`.

When adding a new app or package, create a `pyproject.toml` inside it — UV will automatically pick it up via the glob patterns.

## Adding New Packages/Apps

New packages go in `packages/`, new apps in `apps/`. Each needs its own `pyproject.toml`. To use a local package as a dependency in an app, add it to the root `[tool.uv.sources]` and to the app's `[project.dependencies]`.
