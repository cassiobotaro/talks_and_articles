#!/usr/bin/python3
from collections.abc import Iterable, Iterator

um_a_dez = range(1, 11)

print(type(um_a_dez))

print('Has __iter__?', hasattr(um_a_dez, '__iter__'))

print('Has __next__?', hasattr(um_a_dez, '__next__'))

print('Is iterable?', isinstance(um_a_dez, Iterable))
print('Is iterator?', isinstance(um_a_dez, Iterator))
