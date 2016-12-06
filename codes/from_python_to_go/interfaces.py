#!/usr/bin/python3
from abc import ABCMeta, abstractmethod
# Attention: Bad python code, don't do it in home


class FileLikeObject(metaclass=ABCMeta):

    @abstractmethod
    def read(self):
        raise NotImplementedError()

    @abstractmethod
    def write(self):
        raise NotImplementedError()


class MyFile(FileLikeObject):

    def __init__(self, content):
        self.content = content

    # intentional different signature
    def read(self, int=None):
        if int:
            return self.content[:int]
        return self.content

    def write(self):
        pass


def read_all_content(file_like_object):
    return file_like_object.read()

file_like = FileLikeObject()
content = read_all_content(MyFile('another content'))
print(content)
