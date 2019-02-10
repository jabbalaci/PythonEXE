Python EXE
==========

A simple project that demonstrates how to create an executable
from a Python project.

Here, `hello.py` is the main file. It uses a module (`helper.py`),
it imports the `os` module from the stdlib, and it even uses
a 3rd-party library (`requests`).

With PyInstaller, you can easily create a single executable from
this project.

    $ pyinstaller --onefile hello.py

Under Windows you might have a problem with this. If the .exe complains that
a DLL is missing, then try this variation:

    $ pyinstaller --onefile --noupx hello.py

You'll find the exe in the `dist/` folder.

Why would I need an EXE?
------------------------

It makes distributing your program much easier. The exe produced by
PyInstaller is standalone. It's enough to give this exe to your
friend and (s)he can run it right away. There is no need to install
Python on his/her machine, create a virtual environment, etc.

Of course, if your friend uses Windows (Linux), then create the exe under
Windows (Linux).

pynt
----

[pynt](https://github.com/rags/pynt) is a minimalistic build tool. If you installed everything
with pipenv (`pipenv install --dev`), then you can also create
the executable with the following commands:

    $ pynt exe

or (using pyinstaller's `--noupx` switch)

    $ pynt exe2

Video
-----

Click on the image below to open a YouTube video that shows you everything step-by-step:

<div align="center">
  <a href="https://www.youtube.com/watch?v=2XBjnfx3g3U"><img width="60%" src="assets/screenshot.png" alt="view demo on YouTube"></a>
</div>

Links
-----

Reddit discussion: [here](https://old.reddit.com/r/learnpython/comments/aoxoki/i_made_a_sample_project_to_demonstrate_how_to/).
