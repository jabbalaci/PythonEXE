#!/usr/bin/env python3

"""
demonstrating that you can use modules, libraries,
including 3rd-party libraries
"""

import os

import requests

import helper


def main():
    print('hello world')
    print('contacting google.com...')
    r = requests.head("https://www.google.com")
    print("status code:", r.status_code)
    print("PATH:", os.getenv("PATH"))
    result = helper.add(1, 1)
    print(f"1 + 1 = {result}")

##############################################################################

if __name__ == "__main__":
    main()
