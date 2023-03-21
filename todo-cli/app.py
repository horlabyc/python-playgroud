import typer
from rich.console import Console
from rich.table import Table
from model import Todo
from database import get_all_todos, delete_todo, insert_todo, complete_todo, update_todo

console = Console()
app = typer.Typer()

@app.command(short_help='add a new todo item')
def add(task: str, category: str):
  typer.echo(f"adding {task}, {category}")
  todo = Todo(task, category)
  insert_todo(todo)
  show()

@app.command(short_help='update a todo item')
def update(id: int, task: str = None, category: str = None):
  typer.echo(f"adding {task}, {category}")
  update_todo(id-1, task, category)
  show()

@app.command(short_help='delete a todo item')
def delete(id: int):
  typer.echo(f"deleting {id}")
  delete_todo(id-1)
  show()

@app.command(short_help='complete a todo item')
def complete(id: int):
  typer.echo(f"complete {id}")
  complete_todo(id-1)
  show()

@app.command()
def show():
  tasks = get_all_todos()
  console.print("[bold magenta]Todos[/bold magenta]!",":computer:")

  table = Table(show_header=True, header_style="bold blue")
  table.add_column("id", style="dim", width=6)
  table.add_column("Todo", min_width=20)
  table.add_column("Category", min_width=12, justify="right")
  table.add_column("Done", min_width=12, justify="right")

  def get_category_color(category):
    colors = {'Learn': 'cyan', 'Youtube': 'red', 'Sports': 'cyan', 'Study': 'green'}
    if category in colors:
      return colors[category]
    return 'white'

  for index, task in enumerate(tasks, start=1):
    c = get_category_color(task.category)
    is_done_str = ":white_check_mark:" if task.status == 2 else ":x:"
    table.add_row(str(index), task.task, f'[{c}]{task.category}[/{c}]', is_done_str)
  console.print(table)

if __name__ == "__main__":
  app()