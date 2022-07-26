import typer
from rich import print

app = typer.Typer()

@app.command()
def view():
  """
  View current current templates
  """
  raise NotImplementedError

@app.command()
def add():
  """
  Add a new template
  """
  raise NotImplementedError

@app.command()
def delete():
  """
  Delete a template
  """
  raise NotImplementedError

if __name__ == "__main__":
  app()