# private library of commonly used functions

def read_file_by_line(file):
    fname = open(file, "r")
    fread = fname.read()
    emptylist = []
    pieces = fread.split()
    return pieces


def duplicate(
        thing):  # aggregate data by determining whether a letter is a single or duplicate and placing in appropriate list
    single = []
    dup = []
    values = list(thing)
    for item in values:
        if item not in single:
            single.append(item)
        else:
            dup.append(item)

    return dup
