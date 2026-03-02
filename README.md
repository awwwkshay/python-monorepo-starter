# Python Monorepo Starter

A UV workspace monorepo with a shared `core` library and a FastAPI web application.

## Documentation

- [Getting Started](docs/getting-started.md)
- [Development Guide](docs/development.md)

## Quick Start

```bash
# Install dependencies
uv sync

# Start the API in dev mode (hot-reload)
uv run dev

# Or run directly with FastAPI CLI
uv run fastapi dev apps/api/main.py
```

## Project Structure

```text
.
├── apps/
│   └── api/          # FastAPI web application
├── packages/
│   └── core/         # Shared utility library
└── docs/             # Documentation
```
