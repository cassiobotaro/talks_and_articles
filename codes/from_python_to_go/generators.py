#!/usr/bin/python3


def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        yield a

sequence = fib(10)
print(next(sequence))
print(next(sequence))
print(next(sequence))
print(80 * '-')
for number in fib(10):
    print(number)
