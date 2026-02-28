# syntax=docker/dockerfile:1
# Build context: repo root
#   docker build -f apps/api/Dockerfile -t api .

# ── Builder ────────────────────────────────────────────────────────────────────
FROM python:3.14-slim AS builder

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

WORKDIR /app

# Copy workspace manifests first so dependency installation is cached
# independently from source changes.
COPY pyproject.toml uv.lock ./
COPY apps/api/pyproject.toml ./apps/api/pyproject.toml
COPY packages/core/pyproject.toml ./packages/core/pyproject.toml

# Install external dependencies only (skip workspace packages for now).
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-workspace

# Copy source code.
COPY apps/api/ ./apps/api/
COPY packages/core/ ./packages/core/

# Install workspace packages as built wheels (not editable) so the runtime
# image does not need the packages/core source tree.
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-editable

# ── Runtime ────────────────────────────────────────────────────────────────────
FROM python:3.14-slim

WORKDIR /app

# Bring in the fully-populated virtual environment.
COPY --from=builder /app/.venv /app/.venv

# Only the app source is needed at runtime; core is installed in the venv.
COPY --from=builder /app/apps/api ./apps/api

ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000

CMD ["fastapi", "run", "apps/api/main.py", "--host", "0.0.0.0", "--port", "8000"]
