#!/usr/bin/python3

head, *rest = range(5)

print('head: ', head)

*rest, tail = range(5)

print('tail: ', tail)

head, *rest, tail = range(5)

print(f'head: {head}, tail: {tail}, rest: {rest}')

a_dict = {'a': 1, 'b': 2}
another = {'c': 3, 'd': 4}

merge = {**a_dict, **another}
print(merge)
