import typer
from rich.console import Console
from rich.table import Table

console = Console()
app = typer.Typer()

@app.command(short_help='add a new todo item')
def add(task: str, category: str):
  typer.echo(f"adding {task}, {category}")

@app.command(short_help='update a todo item')
def update(id: str, task: str = None, category: str = None):
  typer.echo(f"adding {task}, {category}")

@app.command(short_help='delete a todo item')
def delete(id: str):
  typer.echo(f"deleting {id}")

@app.command(short_help='complete a todo item')
def complete(id: str):
  typer.echo(f"complete {id}")


if __name__ == "__main__":
  app()