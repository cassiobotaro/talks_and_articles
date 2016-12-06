#!/usr/bin/python3


# let's write a function that handles an exception
def unsafe_division(number1, number2):
    '''Divide number1 by the number2.'''
    return number1 / number2


def main():
    '''Will handles an exception.'''
    try:
        print(unsafe_division(3, 0))
    except ZeroDivisionError as exc:
        print(exc)
    print("Good bye!")

if __name__ == "__main__":
    main()
