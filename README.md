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
git submodule update --remote --init --recursive --merge
```

## TODO list

- [X] Automatically Install missing submodules
- [ ] Be able to install dependencies, build and start an app
  - [X] Install/Update app submodules
  - [X] Build and start
    - [X] Repositories that use Pipenv
    - [X] For normal python apps(and that start with main.py)
  - [ ] Cache data and settings
    - [ ] Make an app start when the os boots up
  - [ ] Stop/Start repositories by name
- [X] Discover repositories locally on the user computer
  - [ ] Improve the function to retrieve subprocesses by cwd, to do this fetch data only once
        and work on that data, instead of calling ps each time to find data.
- [ ] Feedback
  - [ ] Show every repository
    - [ ] And their status, whether they are running or not
  - [ ] Show running apps/repositories
