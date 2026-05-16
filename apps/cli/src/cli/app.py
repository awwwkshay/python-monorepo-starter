import typer
from core import hello as core_hello

app = typer.Typer()


@app.command(name="hello")
def hello(name: str):
    print(core_hello(name))


if __name__ == "__main__":
    app()
