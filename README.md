# Shell Script Template

This repository contains a template for a Python script that uses `argparse` for command-line argument parsing.

## How to Use `argparse`

The `argparse` module makes it easy to write user-friendly command-line interfaces. The program defines what arguments it requires, and `argparse` will figure out how to parse those out of `sys.argv`.

### Adding the Alias

#### For Bash

Add the alias to your `~/.bash_profile` or `~/.bashrc`:

```sh
echo "alias pyscript='/usr/bin/python3 $(pwd)/main.py'" >> ~/.bash_profile
```

OR

```sh
echo "alias pyscript='/usr/bin/python3 $(pwd)/main.py'" >> ~/.bashrc
```

Make sure to reload your profile to apply the changes:

```sh
source ~/.bash_profile
```

```sh
source ~/.bashrc
```

#### For Zsh

Add the alias to your `~/.zshrc`:

```sh
echo "alias pyscript='/usr/bin/python3 $(pwd)/main.py'" >> ~/.zshrc
```

Make sure to reload your profile to apply the changes:

```sh
source ~/.zshrc
```

#### For PowerShell

Add the alias to your PowerShell profile:

```sh
Add-Content -Path $PROFILE -Value "function pyscript { & 'C:\Path\To\Python\python.exe' '$(pwd)\main.py' @args }"
```

Make sure to reload your profile to apply the changes:

```sh
. $PROFILE
```

#### For CMD

Create a batch file named pyscript.bat in a directory that is included in your PATH environment variable:

```sh
@echo off
C:\Path\To\Python\python.exe %~dp0\main.py %*
```

This will add an alias to your shell profile so you can run the script using the `pyscript` command.

### Running the Script

To run the script with a specific directory:

```sh
pyscript --directory /path/to/directory
```

If no directory is specified, the script will use the current working directory by default.

```sh
pyscript
```

For script help, run:

```sh
pyscript --help
```