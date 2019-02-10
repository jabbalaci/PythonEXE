Experimental Results
--------------------

```
(PythonEXE-CCJMp2QJ) $ ./fibo.py
fib(38) = 39088169 was computed in 10.75 seconds
==============================================================================
(PythonEXE-CCJMp2QJ) $ pynt exe2
[ build.py - Starting task "exe2" ]
┌ start: calling external command 'pyinstaller --onefile --noupx fibo.py'
...
└ end: calling external command 'pyinstaller --onefile --noupx fibo.py'
[ build.py - Completed task "exe2" ]
==============================================================================
(PythonEXE-CCJMp2QJ) $ dist/fibo
fib(38) = 39088169 was computed in 11.93 seconds
```

I executed these tests several times and sometimes the runtimes
were very close to each other, and sometimes the gap was wider (like here above).

The point is that the EXE won't run faster.
