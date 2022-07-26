import typer, os, json
from rich import print
from datetime import datetime

# initialize config
app = typer.Typer()


# cli commands
@app.command()
def view():
  """
  View current current templates
  """
  raise NotImplementedError

@app.command()
def add(name: str, path: str):
  """
  Add a new template
  """
  config = load()
  template = {
    "name": name,
    "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  }
  config["templates"].append(template)
  save(config)
  print(f"[bold green] Added template {name}")



@app.command()
def delete():
  """
  Delete a template
  """
  raise NotImplementedError


# utility functions
def load():
  """
  Loads the config file
  """
  if os.path.exists('~/.templater/config.json'):
    with open('~/.templater/config.json', 'r') as f:
      return json.load(f)
  else:
    return {"templates": []}

def save(config):
  """
  Saves the config file
  """
  with open('~/.templater/config.json', 'w') as f:
    json.dump(config, f)


if __name__ == "__main__":
  app()