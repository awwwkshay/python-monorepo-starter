def main() -> None:
    print("Hello from core!")


def hello(name: str) -> str:
    return f"Hello, {name}!"


__all__ = ["main", "hello"]
