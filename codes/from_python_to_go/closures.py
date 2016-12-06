#!/usr/bin/python3


def integer_sequence():
    '''Returns a sequence of integers'''
    i = 0
    def sequence():
        nonlocal i
        i += 1
        return i
    return sequence

next_int = integer_sequence()
print(next_int())
print(next_int())
print(next_int())
