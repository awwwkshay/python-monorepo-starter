# Development Guide

## Package Manager

This project uses [uv](https://github.com/astral-sh/uv) exclusively. Do not use `pip` or `poetry`.

```bash
uv sync                   # Install all workspace dependencies
uv add <package>          # Add a dependency to current package
uv add --dev <package>    # Add a dev dependency
```

## Common Commands

```bash
# Run the API in dev mode (hot-reload)
uv run dev

# Run the API in production mode
uv run start

# Run the core CLI
uv run core

# Lint
uv run ruff check .

# Format
uv run ruff format .

# Type check
uv run ty check
```

## Project Scripts

The `api` package exposes two scripts via `[project.scripts]` in `apps/api/pyproject.toml`:

| Script  | Command        | Description                                    |
|---------|----------------|------------------------------------------------|
| `dev`   | `uv run dev`   | Starts uvicorn with `--reload` for development |
| `start` | `uv run start` | Starts uvicorn without reload for production   |

## Code Style

- Formatting and linting are handled by [ruff](https://github.com/astral-sh/ruff)
- Type checking uses [ty](https://github.com/astral-sh/ty)
- Run both before committing:

```bash
uv run ruff format .
uv run ruff check .
uv run ty check
```
