from abc import ABC, abstractmethod

from fly_behavior import FlyNoWay, FlyWithWings
from quack_behavior import MuteQuack, Quack, Squeak


class Duck(ABC):
    """Template for a duck.

    Encapsulates the behavior of quack and fly, exposing a setter method
    allowing it to change at runtime.
    All ducks can swin (default implementation).
    The usage of ABC and abstractmethod is to force that
    all ducks should have a display method with your own implementation.
    """

    def __init__(self, fly_behavior, quack_behavior):
        self.fly_behavior = fly_behavior
        self.quack_behavior = quack_behavior

    @abstractmethod
    def display(self):
        """If not implemented by its subclasses, it cannot be instantiated."""
        raise NotImplementedError

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()

    def swin(self):
        print("All ducks float, even decoys!")

    # setter methods
    def set_quack_behavior(self, qb):
        self.quack_behavior = qb

    def set_fly_behavior(self, fb):
        self.fly_behavior = fb


class MallardDuck(Duck):
    """Mallard duck IS-A duck.

    It shares encapsulation of fly and quack behaviors,
    setting concrete implementation of this behaviors.
    Specializes the method display with your own implementation.
    As a Duck, MallardDucks also can swin.
    """

    def __init__(self):
        # override the method with pre defined values
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def display(self):
        print("I'm a real Mallard duck")


class RubberDuck(Duck):
    """Rubber Duck IS-A duck.

    It shares encapsulation of fly and quack behaviors,
    setting concrete implementation of this behaviors.
    Rubber ducks cannot fly and make squeak instead of quack.
    Specializes the method display with your own implementation.
    As a Duck, RubberDucks also can swin.
    """
    def __init__(self):
        # override the method with pre defined values
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = Squeak()

    def display(self):
        print("I'm a rubber duck")


class DecoyDuck(Duck):
    """Decoy Duck IS-A duck.

    It shares encapsulation of fly and quack behaviors,
    setting concrete implementation of this behaviors.
    Decoy ducks cannot fly and cannot make sound.
    Specializes the method display with your own implementation.
    As a Duck, DecoyDucks also can swin (?!).
    """

    def __init__(self):
        # override the method with pre defined values
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = MuteQuack()

    def display(self):
        print("I'm a decoy duck")


class ModelDuck(Duck):
    """Model Duck IS-A duck.

    It shares encapsulation of fly and quack behaviors,
    setting concrete implementation of this behaviors.
    Specializes the method display with your own implementation.
    As a Duck, ModelDucks also can swin.
    """
    def __init__(self):
        # override the method with pre defined values
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = Quack()

    def display(self):
        print("I'm a model duck")

# Easy to create new ducks without change the legacy code.
