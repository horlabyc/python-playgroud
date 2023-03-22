import typer
from rich.console import Console
from rich.table import Table

from repository import get_all_stocks, insert_stock, reduce_stock_quantity, increase_stock_quantity, delete_stock
from model import StockItem

console = Console()
app = typer.Typer()

@app.command(short_help="show all stocks")
def add(name: str, quantity: int, category: str):
    typer.echo(f"Adding new stock...")
    new_stock = StockItem(name, category, quantity)
    insert_stock(new_stock)
    show()

@app.command(short_help="reduce stock quantity")
def reduce_stock(id: int, quantity: int):
    typer.echo(f"Reducing stock quantity...")
    reduce_stock_quantity(id, quantity)
    show()

@app.command(short_help="increase stock quantity")
def increase_stock(id: int, quantity: int):
    typer.echo(f"Increasing stock quantity...")
    increase_stock_quantity(id, quantity)
    show()

@app.command(short_help="clear stock")
def clear_stock(id: int):
    typer.echo(f"Clearing stock...")
    delete_stock(id)
    show()

@app.command(short_help="show all stocks")
def show():
    stocks = get_all_stocks()
    console.print("[bold magenta]-=-=-=-=-=-Stock Tracker Application-=-=-=-=-=-[/bold magenta]",":notebook_with_decorative_cover:") 

    table = Table(show_header=True, header_style="bold blue")
    table.add_column("id", style="dim", width=6)
    table.add_column("Name", min_width=20)
    table.add_column("Category", min_width=20, justify="center")
    table.add_column("Quantity", min_width=12, justify="center")
    table.add_column("Created date", min_width=20, justify="center")
    table.add_column("Status", min_width=20, justify="center")


    for _, stock in enumerate(stocks):
        depleted = ":red_circle:" if int(stock.quantity) < 1 else ":green_circle:"
        table.add_row(str(stock.id), stock.name, stock.category, str(stock.quantity), stock.created_at, depleted)
    console.print(table)


if __name__ == "__main__":
    app()