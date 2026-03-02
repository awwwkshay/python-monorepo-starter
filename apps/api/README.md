# api

FastAPI web application. Depends on the `core` package.

## Endpoints

### `GET /health`

Returns the health status of the API.

```json
{ "status": "healthy" }
```

### `GET /hello/{name}`

Returns a greeting for the given name.

```json
{ "message": "Hello, {name}!" }
```

## Scripts

| Script  | Command        | Description                                    |
|---------|----------------|------------------------------------------------|
| `dev`   | `uv run dev`   | Starts uvicorn with `--reload` for development |
| `start` | `uv run start` | Starts uvicorn without reload for production   |

## Docker

```bash
docker build -t api .
docker run -p 8000:8000 api
```

## Interactive Docs

Available when the server is running:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
