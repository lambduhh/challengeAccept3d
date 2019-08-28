# Given an integral number, determine if it's a square number
# separation of concerns (business logic vs render logic)
# decoupling
import math


def print_results(r: tuple) -> None:  # one arg, r that is a tuple and will result in None
    (n, result) = r
    if isinstance(result, ValueError):  # is e an instance of a ValueError?
        print("number is negative, try again")
    elif result is False:
        print(n, "is not a square")
    else:
        print(n, "is a perf square")


def could_be_int(x):
    if x % 1 == 0:
        return True


def is_square(n):
    try:
        x = math.sqrt(n)
    except ValueError as result:
        return n, result  # return a neg number, a ValueError
    else:
        if could_be_int(x):
            result = True
            return n, result  # is a perfect sq, returns n, result =True
    result = False
    return n, result  # n is not a perfect sq, returns n, result= False


if __name__ == '__main__':
    r = is_square(-19)
    print_results(r)
