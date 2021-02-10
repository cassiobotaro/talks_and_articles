from abc import ABC, abstractmethod
# ABC is used to formalize an interface.
# Given the dynamic nature of python, this definition would not be necessary,
# every instance of a class that has the quack method could be
# considered a quacking behavior.
# Each class have your own implementation of method quack.
# Program to interface not the implementation.
# Do not confuse with the reserved word interface of some languages.
# The concept here has to do with the way in which
# objects communicate (messages).


class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        raise NotImplementedError


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I'm flying")


class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I can't fly")


class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print("I'm flying with a rocket")

# FlyBehavior is easy to extend.
# Instead of conditional (if) use a class to represent
# negative behaviors (FlyNoWay)
