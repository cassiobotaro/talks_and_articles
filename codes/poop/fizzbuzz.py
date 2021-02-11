# smalltalk infected fizzbuzz version
from forbiddenfruit import curse
from collections import deque


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


def println(self):
    """Prints the values to a stream, or to sys.stdout by default.

    >>> "Fizz".print()
    Fizz
    >>> "FizzBuzz".print()
    FizzBuzz
    """
    print(self)


def do(self, block):
    """Evaluate the receiver for each element in aBlock.

    >>> range(1, 11).do(lambda number: number.print())
    """
    deque(map(block, self), maxlen=0)
    return self


curse(bool, "if_true", if_true)
curse(bool, "if_false", if_false)
curse(str, "print", println)
curse(int, "print", println)
curse(range, "do", do)

# lambdas are used to simulate blocks
"""Summary
We add a do methd on range objects that evaluates a block
for each element on interval.
This block will receive a number, that evaluated
in the expression "number % 15 == 0", This will result in a boolean object,
to which we will send two messages,
one with a block to be evaluated if the expression is true and
another for if it is false.
If true, we will send a print message to a "FizzBuzz" object.
If it is false, we will use the same numeric object
to evaluate the expression number% 5 == 0.
And so we repeat the cycle, until at last a message
is sent to the number printed.
"""
range(1, 101).do(
    lambda number: (number % 15 == 0)
    .if_true("FizzBuzz".print)
    .if_false(
        lambda: (number % 5 == 0)
        .if_true("Buzz".print)
        .if_false(
            lambda: (number % 3 == 0)
            .if_true("Fizz".print)
            .if_false(number.print)
        )
    )
)

"""
Notes:
- A message is sent to an object for printing
- Lambdas are used to simulate a block
- Add method do for a range, evaluating a block on each number on interval
- Objects and messages
"""
