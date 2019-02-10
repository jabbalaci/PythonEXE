#!/usr/bin/env python3

"""
pynt's build file
https://github.com/rags/pynt

Usage:

$ pynt
"""

import os
from pynt import task


def call_external_command(cmd):
    print(f"┌ start: calling external command '{cmd}'")
    os.system(cmd)
    print(f"└ end: calling external command '{cmd}'")

###########
## Tasks ##
###########

@task()
def exe():
    """
    create executable with PyInstaller
    """
    call_external_command("pyinstaller --onefile fibo.py")


@task()
def exe2():
    """
    create executable with PyInstaller (--noupx)
    """
    call_external_command("pyinstaller --onefile --noupx fibo.py")
