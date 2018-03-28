#!/usr/bin/python3
import io
from contextlib import redirect_stdout

f = io.StringIO()
with redirect_stdout(f):
    import fake_module
f.seek(0)
print("suppresed output: ", f.read())

# old style
# https://github.com/keras-team/keras/issues/1406
# import sys
# import io
# stdout = sys.stdout
# sys.stdout = io.StringIO()
# import this
# sys.stdout = stdout
# example keras
