# Python app manager

Python app manager is to start and stop python apps and install dependencies \
when required.

This project will grow as long as I need it to grow in the aspects I need,
what I mean is that I will not code extra functionality that I won't ever
use.

## Packages required

This module uses these packages:
* [Pipenv](https://github.com/pypa/pipenv)
* [Toml 0.10.2](https://pypi.org/project/toml/)
* psutil

## Submodules

This repository uses the following submodule/s:
* [Process utils](https://github.com/Perseverancia-company/sub.process-utils)

The program automatically installs/updates the submodules using the following command:


```bash
submodule update --remote --init --recursive --merge
```

## TODO list

- [X] Automatically Install missing submodules
- [ ] Be able to install dependencies, build and start an app
  - [X] For normal python apps(and that start with main.py)
  - [ ] For Django apps
- [ ] Discover repositories locally on the user computer
- [ ] Be able to clone/pull user repositories

