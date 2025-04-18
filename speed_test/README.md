Experimental Results
--------------------

```
(PythonEXE-CCJMp2QJ) $ ./fibo.py
fib(38) = 39088169 was computed in 10.75 seconds
==============================================================================
(PythonEXE-CCJMp2QJ) $ make exe2
pyinstaller --onefile --noupx fibo.py
...
==============================================================================
(PythonEXE-CCJMp2QJ) $ dist/fibo
fib(38) = 39088169 was computed in 11.93 seconds
```

I executed these tests several times and sometimes the runtimes
were very close to each other, and sometimes the gap was wider (like here above).

The point is that the EXE won't run faster.
