#!/usr/bin/env python3

"""
demonstrating that you can use modules, libraries,
including 3rd-party libraries
"""

import os
import sys
from pathlib import Path

import requests

import helper

BASE_DIR = os.path.dirname(os.path.abspath(sys.argv[0]))


def main():
    print("hello world")
    print("contacting google.com...")
    r = requests.head("https://www.google.com")
    print("status code:", r.status_code)
    print("PATH:", os.getenv("PATH"))
    result = helper.add(1, 1)
    print(f"1 + 1 = {result}")
    try:
        with open(Path(BASE_DIR, "input.txt")) as f:
            content = f.read().strip()
        print(content)
    except IOError:
        print("Warning: input.txt was not found")
    #
    fname = Path(BASE_DIR, "output.txt")
    print("writing to the following file:", fname)
    with open(fname, "w") as g:
        print("writing to a file", file=g)


##############################################################################

if __name__ == "__main__":
    main()
