#!/usr/bin/python3
from typing import List, IO, Sized

# annotate a variable
spam: str = "eggs spam bacon spam"


def square(list_of_numbers: List[int]) -> List[int]:
    return [number ** 2 for number in list_of_numbers]


def printlines(file: IO) -> None:
    for line in file:
        print(f'{line}\n')


def printsize(sized: Sized):
    print(len(sized))


# don't validate type
spanish_inquisition: str
