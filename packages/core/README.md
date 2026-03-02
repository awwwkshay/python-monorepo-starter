# core

Shared utility library used across apps in the monorepo. No external dependencies.

## Usage

```python
from core import hello, main

hello("world")  # "Hello, world!"
main()          # prints "Hello from core!"
```

## API

### `hello(name: str) -> str`

Returns a greeting string for the given name.

### `main() -> None`

Prints a greeting message to stdout. Used as the CLI entry point (`uv run core`).
