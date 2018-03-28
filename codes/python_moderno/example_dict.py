#!/usr/bin/python3
from collections.abc import Iterable, Iterator

some_dict = {'a': 1, 'b': 2}
keys = some_dict.keys()

print(type(keys))

print(keys & {'a', 'b'})
print(keys | {'a', 'b'})
print(keys ^ {'a', 'b'})

print('Is iterable?', isinstance(keys, Iterable))
print('Is iterator?', isinstance(keys, Iterator))
