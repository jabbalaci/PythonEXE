#!/usr/bin/env python3

import time

X = 38


def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def main():
    start = time.time()
    res = fib(X)
    elapsed = time.time() - start
    print("Py3 Computed fib(%s)=%s in %0.2f seconds" % (X, res, elapsed))

##############################################################################

if __name__ == "__main__":
    main()
