#!/usr/bin/python3
from contextlib import suppress

d = {1: 'one', 2: 'two'}
with suppress(KeyError):
    print(d[3])

# old style
# try:
#   print(d[3])
# except KeyError:
#   pass
