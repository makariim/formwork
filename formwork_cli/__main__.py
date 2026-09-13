"""So the kit works even when the `formwork` command is not on your path.

    python3 -m formwork_cli check

`pip install` puts the command in a scripts folder that is frequently not on
somebody's path, and the only sign of it is `formwork: command not found` with
nothing explaining why. Installing with pipx or into a virtual environment
avoids that, and this is the way through for anybody who has already installed
it the other way.

Running the module uses the interpreter you named, so it cannot pick the wrong
one. That is the same reason `python3 -m pip install` is safer than `pip`.
"""
import sys

from . import main

if __name__ == "__main__":
    sys.exit(main())
