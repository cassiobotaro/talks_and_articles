# based on talk Nothing is something - Sandi Metz
# https://www.youtube.com/watch?v=OMPfEXIlTVE&t=562s&ab_channel=Confreaks

# send message to object 1 to call method bit_length
(1).bit_length()
# another way to do the same
getattr(1, "bit_length")()
# call builtin str on number 1, returning a string object
str(1)
# we can call dunder str, it's equivalent, but it's not recommended
(1).__str__()
# send message __str__ to object and call method
getattr(1, "__str__")()

# access object class
(1).__class__

# different from ruby, True and False are instances of bool
(True).__class__
(False).__class__

# truthy objects in python are objects that __bool__ returns True
# falsy returns False


class Truthy:
    def __bool__(self):
        return True


# messsage sending syntax for booleans


def if_true(self, block):
    # simulate blocks using functions
    self and block()
    # close circuit when object is truthy
    return self


def if_false(self, block):
    # simulate blocks using functions
    not self and block()
    # close circuit when object is falsy
    return self


# let's curse booleans
from forbiddenfruit import curse

# We are adding two new methods for builtin bool class
curse(bool, "if_true", if_true)
curse(bool, "if_false", if_false)

# use message instead of conditional
# As the expression is truthy, block is evaluated
(1 == 1).if_true(lambda: print("evaluated block"))
# Not evaluated because expression is truthy
(1 == 1).if_false(lambda: print("block is ignored"))
# As the expression is false, block is not evaluated
(1 == 2).if_true(lambda: print("block is ignored"))
# Evaluated beacuse expression is falsy
(1 == 2).if_false(lambda: print("evaluated block"))

# remembering that any object can be truthy or falsy
# let's curse object class
curse(object, "if_true", if_true)
curse(object, "if_false", if_false)

"anything".if_true(lambda: print("evaluated block"))
"anything".if_false(lambda: print("ignored block"))

None.if_true(lambda: print("ignored block"))
None.if_false(lambda: print("evaluated block"))

# It's not about change Python
# It's a question of avoid if's and change your mindset

# This class emulate something that looks like an ORM


class Animal:

    # just to emulate some content
    repository = ["pig", "sheep"]

    def __init__(self, name):
        self.name = name

    @classmethod
    def find(cls, id_):
        if id_ not in cls.repository:
            return None
        return cls(id_)

    def __str__(self):
        return f"Animal({self.name})"


# returns an animal if it exists else None
print(Animal.find("pig"))
print(Animal.find(""))

ids = ["pig", "", "sheep"]

# In python, sequence objets like list don't have
# a map method, instead we have a builtin function
# map that receives one or many iterables(objects that
# follow iterable protocol)
animals = map(Animal.find, ids)

# we also don't have an each method
# code below will fail
# for animal in animals:
#     print(animal.name)

# note: map and for are not SmallTalk infected but
# I decided to maintain it for now

# If you send it a message, nil is something. - Sandi Metz

# using try
# for animal in animals:
#     try:
#         print(animal.name)
#     except AttributeError:
#         print("no animal")
# try is an if that depends on code execution
# and then maybe I have this conditional in a lot of places


class MissingAnimal:
    @property
    def name(self):
        return "no animal"


# wrap to avoid repeat if
# in many places
class GuaranteedAnimal:
    @classmethod
    def find(cls, id_):
        return Animal.find(id_) or MissingAnimal()


# use guaranteed animals and sure that an animal will be returned
animals = map(GuaranteedAnimal.find, ids)
for animal in animals:
    print(animal.name)

# OOP is about objects and messages

# A class house that recites the text
# class House:
#     @property
#     def data(self):
#         return [
#             "the horse and the hound and the horn that belonged to",
#             "the farmer sowing his corn that kept",
#             "the rooster that crowed in the morn that woke",
#             "the priest all shaven and shorn that married",
#             "the man all tattered and torn that kissed",
#             "the maiden all forlorn that milked",
#             "the cow with the crumpled horn that tossed",
#             "the dog that worried",
#             "the cat that killed",
#             "the rat that ate",
#             "the malt that lay in",
#             "the house that Jack built",
#         ]

#     def recite(self):
#         return "\n".join(self.line(i) for i, _ in enumerate(self.data, 1))

#     def line(self, number):
#         return f"This  is {self._phrase(number)}\n"

#     def _phrase(self, number):
#         return " ".join(self.data[-number:])


# print(House().line(12))
# print(House().recite())

import random
from functools import cached_property


def shuffle(self):
    """Shuffle the sequence x in place.

    >>> [1, 2, 3].shuffle()
    [3, 1, 2]
    """
    data = self.copy()
    random.shuffle(data)
    return data


# just for fun, I'll add a shuffle method on lists
curse(list, "shuffle", shuffle)

# RandomHouse IS-A house that randomize the text
# class RandomHouse(House):
#     @cached_property
#     def data(self):
#         return super().data.shuffle()


# randomhouse = RandomHouse()
# print(randomhouse.line(1))
# print(randomhouse.line(2))
# print(randomhouse.line(3))
# print(randomhouse.line(12))


# class House:
#     @property
#     def data(self):
#         return [
#             "the horse and the hound and the horn that belonged to",
#             "the farmer sowing his corn that kept",
#             "the rooster that crowed in the morn that woke",
#             "the priest all shaven and shorn that married",
#             "the man all tattered and torn that kissed",
#             "the maiden all forlorn that milked",
#             "the cow with the crumpled horn that tossed",
#             "the dog that worried",
#             "the cat that killed",
#             "the rat that ate",
#             "the malt that lay in",
#             "the house that Jack built",
#         ]

#     def recite(self):
#         return "\n".join(self.line(i) for i, _ in enumerate(self.data, 1))

#     def line(self, number):
#         return f"This  is {self._phrase(number)}\n"

#     def parts(self, number):
#         return self.data[-number:]

#     def _phrase(self, number):
#         return " ".join(self.parts(number))


# print(House().parts(3))
# print(House().line(12))
# print(House().recite())


from itertools import chain


def zip_(self, iterable):
    """A zip object yielding tuples until an input is exhausted.

    >>> [1, 2, 3].zip([1, 2, 3])
    [(1, 1), (2, 2), (3, 3)]

    >>> [1, 2, 3].zip([3, 2])
    [(1, 3), (2, 2)]
    """
    return list(zip(self, iterable))


def flatten(self):
    """Return a copy of the array collapsed into one dimension.

    >>> [(1, 1), (2, 2), (3, 3)].flatten()
    [1, 1, 2, 2, 3, 3]
    """
    return list(chain.from_iterable(self))


# just for fun again
curse(list, "zip", zip_)
curse(list, "flatten", flatten)

# EchoHouse IS-A House that echo parts
# class EchoHouse(House):
#     def parts(self, number):
#         data = super().parts(number)
#         return data.zip(data).flatten()


# print(EchoHouse().line(1))
# print(EchoHouse().line(2))
# print(EchoHouse().line(3))
# print(EchoHouse().line(12))

# more classes, less if's
# abstract behavior


class DefaultOrder:
    def order(self, data):
        return data


class RandomOrder:
    def order(self, data):
        return data.shuffle()


class DefaultFormatter:
    def format(self, parts):
        return parts


class EchoFormatter:
    def format(self, parts):
        return parts.zip(parts).flatten()


class House:
    DATA = [
        "the horse and the hound and the horn that belonged to",
        "the farmer sowing his corn that kept",
        "the rooster that crowed in the morn that woke",
        "the priest all shaven and shorn that married",
        "the man all tattered and torn that kissed",
        "the maiden all forlorn that milked",
        "the cow with the crumpled horn that tossed",
        "the dog that worried",
        "the cat that killed",
        "the rat that ate",
        "the malt that lay in",
        "the house that Jack built",
    ]

    def __init__(self, orderer=DefaultOrder(), formatter=DefaultFormatter()):
        self.formatter = formatter
        self.data = orderer.order(self.DATA)

    def recite(self):
        return "\n".join(self.line(i) for i, _ in enumerate(self.data, 1))

    def line(self, number):
        return f"This  is {self._phrase(number)}\n"

    def parts(self, number):
        return self.formatter.format(self.data[-number:])

    def _phrase(self, number):
        return " ".join(self.parts(number))


print(House().line(12))
print(House(RandomOrder()).line(12))
print(House(formatter=EchoFormatter()).line(12))

# inject an object to play the role of the thing that varies

# House HAVE an ORDERER ROLE
# House HAVE a  FORMATTER ROLE

# It's composition + dependency injection
# abstraction seeking!!!

# inheritance is not for sharing behavior

# isolate the thing that varies
# name the concept
# define the rola
# inject the players
