#!/usr/bin/python3
from collections import namedtuple

variable = 42

Point = namedtuple('Point', ['long', 'lat'])

point = Point(long=3, lat=4)


def function(number):
    return number ** 2


print(f'{variable}')

print(f'Longitude: {point.long}, Latitude: {point.lat}')

print(f'{function(variable)}')
