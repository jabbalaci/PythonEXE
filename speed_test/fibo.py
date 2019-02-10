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
    result = fib(X)
    elapsed = time.time() - start
    print(f"fib({X}) = {result} was computed in {elapsed:.2f} seconds")

##############################################################################

if __name__ == "__main__":
    main()
