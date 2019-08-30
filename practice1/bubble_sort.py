# Bubble sort is a comparison​-based algorithm that
# compares each pair of elements in an array and swaps them if
# they are out of order until the entire array is sorted.
# -Given an array implement bubblesort on the array and return a list of sorted numbers.


def compare(x, y, swap):
    # fn that can compare the value of 2 numbers and swap if necessary;
    if x < y:
        z = x, y
        swap = swap or False
    else:
        z = y, x
        swap = True
    return z, swap  # returns swapped numbers and new value of swap


def bubble(l):
    is_sorted = False
    while not is_sorted:  # code runs only if the value of is_sorted is False
        idx = 0
        swap = False
        for _ in l[:-1]:  # iterate until next to last thing
            #  call the compare fn using idx placeholders and swap as arguments
            (l[idx], l[idx + 1]), swap = compare(l[idx], l[idx + 1], swap)
            idx = idx + 1  # keep iterating though
        if swap is False:
            is_sorted = True
    return l


def render(l: list) -> None:
    print(l)
    return None


if __name__ == '__main__':
    lll = [3, 2, 5, 1]
    p_results = bubble(lll)
    render(p_results)
