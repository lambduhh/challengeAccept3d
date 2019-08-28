# # Given an string of integers, find the sum of its elements.

#
# Print the sum of the array's elements as a single integer.


def simplearraysum(y):
    l = y.split()  # type conversion  str-> list of ints
    ml = list(map(int, l))
    summ = sum(ml)
    return summ


def print_res(n: int) -> None:
    print(n)


if __name__ == '__main__':
    ipt = "1 2 3 4 5"
    pr = simplearraysum(ipt)
    print_res(pr)
