# py-templater

![pypi build](https://img.shields.io/github/workflow/status/h3x4g0ns/py-templater/pypi-build)
[![PyPI version](https://badge.fury.io/py/py-templater.svg)](https://badge.fury.io/py/py-templater)

## About this Project

Python utility tool that generates code files from user-defined templates. Save files/directories and user-defined templates, and load them on the fly whenever you need access to your boilerplate templates.

## Getting Started

### Prerequisites

You will need `typer` and `rich` in order to use `py-templater`. These should install as dependencies by default.

```sh
pip install py-templater typer rich
```

> ⚠️ Warning<br>
> `py-templater` only works on Linux and macOS machines

### Usage

```sh
templater --help
                                                                                                                   
  Usage: templater [OPTIONS] COMMAND [ARGS]...                                                                      
                                                                                                                   
Options
  --install-completion          Install completion for the current shell.                                        
  --show-completion             Show completion for the current shell, to copy it or customize the installation.
  --help                        Show this message and exit.

Commands
  add       Add a new template
  gen       Generates file(s) from templates
  list      List current current templates
  rm        Delete a template
```

#### `add`

```sh
templater add --help

  Usage: templater add [OPTIONS] NAME PATH

Arguments
  name      template name
  path      path to original file/directory
```

