# private library of commonly used functions
from typing import List, Any


def read_file_by_line(file):
    fname = open(file, "r")
    fread = fname.read()
    emptylist = []
    pieces = fread.split()
    return pieces


def duplicate(
        thing):  # aggregate data by determining whether a letter is a single or duplicate and placing in appropriate list
    single = []
    dup = []  # type: List
    values = list(thing)
    for item in values:
        if item not in single:
            single.append(item)
        else:
            dup.append(item)

    return dup


if __name__ == '__main__':
    p = duplicate(["b", "a", "b", "a", "b", "c", "b", "b", "b"])
    print(p)
    print(duplicate(p))


def convert_str_to_lst(s: str):
    l = []
    for letter in s:
        l.append(letter)
    return l