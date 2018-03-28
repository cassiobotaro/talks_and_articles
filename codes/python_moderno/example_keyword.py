#!/usr/bin/python3
import shutil


def function(parameter1, parameter2, parameter3, kill=False):
    if kill:
        shutil.rmtree('/')
    ...


function(1, 2, 3)
