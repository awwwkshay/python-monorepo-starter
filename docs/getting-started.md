# Getting Started

## Prerequisites

- Python 3.14+
- [uv](https://github.com/astral-sh/uv) package manager

Install uv:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Installation

Clone the repository and install all workspace dependencies:

```bash
git clone <repo-url>
cd python-monorepo-starter
uv sync
```

## Running the API

**Development** (hot-reload enabled):

```bash
uv run dev
```

**Production**:

```bash
uv run start
```

The API will be available at `http://localhost:8000`.

## Running with Docker

```bash
cd apps/api
docker build -t api .
docker run -p 8000:8000 api
```
