#!/usr/bin/python3


class CustomException(IOError):
    ...


try:
    open('naoexistente.txt')
except FileNotFoundError:
    raise CustomException('Something Happens') from FileNotFoundError
