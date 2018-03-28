#!/usr/bin/python3
from collections.abc import Iterator


def square(number):
    return number * number


def odd(number):
    return number % 2 != 0


map_result = map(square, [1, 2, 3])
for number in map_result:
    print(number)
print('Is iterator?', isinstance(map_result, Iterator))
next(map_result)

filter_result = filter(odd, range(10))
for number in filter_result:
    print(number)
print('Is iterator?', isinstance(filter_result, Iterator))
print('Is iterator?', isinstance(zip((1, 2, 3), (4, 5, 6)), Iterator))
