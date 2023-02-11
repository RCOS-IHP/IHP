import sys

from typing import Never

def display_fatal_error(msg: str) -> Never:
    print(msg, file=sys.stderr)
    sys.exit(1)