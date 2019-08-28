# # Given an array of integers, find the sum of its elements.
# Input Format
# The first line contains an integer, , denoting the size of the array.
# The second line contains  space-separated integers representing the array's elements.
# Output Format
#
# Print the sum of the array's elements as a single integer.


def simplearraysum(y):
    l = y.split()
    ml = list(map(int, l))
    summ = sum(ml)
    return summ


def print_res(n: int) -> None:
    print(n)


if __name__ == '__main__':
    ipt = "1 2 3 4 5"
    pr = simplearraysum(ipt)
    print_res(pr)
