# Bob is preparing to pass IQ test.
# The most frequent task in this test is to find out which one of the given numbers
# differs from the others. Bob observed that one number usually differs from the
# others in evenness. Help Bob — to check his answers, he needs a program that
# among the given numbers finds one that is different in evenness, and return a
# position of this number.
#
# ##Examples :
#
# iq_test("2 4 7 8 10") => 3 //
# Third number is odd, while the rest of the numbers are even
#
# iq_test("1 2 1 1") => 2 //
# Second number is even, while the rest of the numbers are odd


# This is a refactored solution of even_is_odd featuring
# higher order functions and functional thought processes


def print_results(r: tuple) -> None:   # r: will be a tuple -> this fn returns None
    ff, which = r                      # r is a tuple of ff, and which
    print("I have", which, "in position", ff)  # the ONLY print statement in the code
    return None


def even_or_odd(n):
    if (n % 2) == 0:
        return "even"
    else:
        return "odd"


def found_odd(nums):
    position = 1
    for n in nums:
        if even_or_odd(n) == "odd":
            return position
        position += 1  # p = p + 1
    return False


def found_even(nums):
    position = 1
    for n in nums:
        if even_or_odd(n) == "even":
            return position
        position += 1  # p = p + 1
    return False


def categorize(nl):  # cat picks the right fn to use to find position
    e = []
    o = []
    for n in nl:
        if n == 'even':
            e.append(n)
        else:
            o.append(n)
    if len(e) == 1:
        return found_odd  # refer to found_odd fn
    else:
        return found_even  # refer to found_even fn


def check_list(l):
    finder_fn = categorize(l)
    which = finder_fn.__name__
    print(which)  # prints name of fn used
    return finder_fn(l), which


if __name__ == '__main__':
    l = [1, 1, 1, 2]
    pr1 = check_list(l)
    print(pr1)
    print_results(pr1)
