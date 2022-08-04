from platform import python_branch
import typer, os, json
from rich import print
from rich.table import Table
from rich.syntax import Syntax
from datetime import datetime
from os import walk
from itertools import islice

# initialize config
app = typer.Typer()
config_path = f"{os.path.expanduser('~/.templater')}"

# cli commands
@app.command()
def gen(name: str = typer.Argument(..., help="template name")):
  """
  Generates file(s) from templates
  """
  config = load()
  if name not in [t["name"] for t in config["templates"]]:
    print(f"[bold red]\"{name}\" Template does not exist")
    return 

  template = [t for t in config["templates"] if t["name"] == name][0]
  ori_path = os.path.join(template["path"], "*")
  os.popen(f"cp -r {ori_path} .")
  print(f"[bold blue]Successfully generated {name}")


@app.command()
def list():
  """
  List current current templates
  """
  config = load()
  table = Table("", "Name", "Created", show_header=True, header_style="bold blue")
  for i, template in enumerate(config["templates"]):
    table.add_row(str(i), template["name"], template["created"])
  print(table)


@app.command()
def add(name: str = typer.Argument(..., help="template name"), path: str = typer.Argument(..., help="path to original file/directory")):
  """
  Add a new template
  """
  config = load()
  if name in [t["name"] for t in config["templates"]]:
    print(f"[bold red]\"{name}\" Template already exists")
    return 

  new_path = os.path.join(config_path, name)
  os.makedirs(new_path)
  os.popen(f"cp -r {path} {new_path}/{path}")
  template = {
    "name": name,
    "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "path": new_path
  }
  config["templates"].append(template)
  save(config)
  print(f"[bold green] Added template {name}")


@app.command()
def rm(name: str = typer.Argument(..., help="template name")):
  """
  Delete a template
  """
  config = load()
  template = [t for t in config["templates"] if t["name"] == name]
  assert len(template) == 1, f"[bold red]\"{name}\" Template does not exist"

  path = template[0]["path"]
  os.popen(f"rm -rf {path}")
  config["templates"].remove(template[0])
  save(config)
  print(f"[bold green] Deleted template {name}")


@app.command()
def view(name: str = typer.Argument(..., help="template name"), n: int = typer.Argument(5, help="lines of code to view")):
  """
  View snippet of template
  """
  config = load()
  template = [t for t in config["templates"] if t["name"] == name]
  assert len(template) == 1, f"[bold red]\"{name}\" Template does not exist"

  path = template[0]["path"]
  files, content = [], []
  for (_, _, filenames) in walk(path):
      files.extend(filenames)
  new_path = os.path.join(path, files[0])
  with open(new_path) as f:
    for _ in range(n):
      content.append(f.readline())
  name = template[0]["name"]
  _, ext = os.path.splitext(new_path)
  print(f"\n[bold blue]{name} contents:")
  print(Syntax("".join(content), ext[1:], theme="gruvbox-dark", line_numbers=True))


# utility functions
def load():
  """
  Loads the config file
  """
  path = os.path.join(config_path, 'config.json')
  if os.path.exists(path):
    with open(path, 'r') as f:
      return json.load(f)
  else:
    return {"templates": []}

def save(config):
  """
  Saves the config file
  """
  os.makedirs(config_path, exist_ok=True)
  path = os.path.join(config_path, 'config.json')
  with open(path, 'w') as f:
    json.dump(config, f)

def _sync(config):
  pass


if __name__ == "__main__":
  app()
