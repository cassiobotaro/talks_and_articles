#!/usr/bin/python3

import secrets

print(secrets.token_bytes(24))

print(len(secrets.token_bytes(24)))


# old style
# import os
# os.urandom(24)
# example: http://flask.pocoo.org/docs/0.12/quickstart/
