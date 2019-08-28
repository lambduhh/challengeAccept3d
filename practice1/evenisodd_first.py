# Bob is preparing to pass IQ test.
# The most frequent task in this test is to find out which one of the given numbers
# differs from the others. Bob observed that one number usually differs from the
# others in evenness. Help Bob — to check his answers, he needs a program that
# among the given numbers finds one that is different in evenness, and return a
# position of this number.
#
# ! Keep in mind that your task is to help Bob solve a real IQ test,
# which means indexes of the elements start from 1 (not 0)
#
# ##Examples :
#
# iq_test("2 4 7 8 10") => 3 //
# Third number is odd, while the rest of the numbers are even
#
# iq_test("1 2 1 1") => 2 //
# Second number is even, while the rest of the numbers are odd


#

list_is_odd = "Most of this list is odd"
list_is_even = "Most of this list is even"


def print_results(r: tuple) -> None:  # r will be a tuple, the fn will return None
    (nl, position, l, cat) = r  # the data in the tuple that is r
    print(cat, "but the number in position", position,
          "is not")  # only one print statement in all of the code = clean code
    return None


def even_or_odd(n):  # even_or_odd uses good ole modulo to figure out if a number is even or odd
    if (n % 2) == 0:
        return "even"  # use of return statements, not print statements
    else:
        return "odd"


def categorize(nl):  # aggregates data
    e = []  # this will be a list of even numbers
    o = []  # list of odd numbers
    for n in nl:
        if n == 'even':
            e.append(n)  # adds even numbers to appropriate list
        else:
            o.append(n)
    if len(e) == 1:  # determines which list is longer
        return list_is_odd
    else:
        return list_is_even


def check_list(l):
    nl = list(map(even_or_odd, l))  # applys even_or_odd fn to list
    if categorize(nl) == list_is_even:
        position = nl.index('odd') + 1  # finds position of odd one out
    else:
        position = nl.index('even') + 1
    return nl, position, l, categorize(nl)  # returns data to pass to print res


if __name__ == '__main__':
    lll = [2, 2, 2, 1]
    pr1 = check_list(lll)

    print_results(pr1)
