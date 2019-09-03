# The goal of this exercise is to convert a string to a new string where
# each character in the new string is "(" if that character appears only once in the
# original string, or ")" if that character appears more than once in the original
# string. Ignore capitalization when determining if a character is a duplicate.
from practice1.utils import duplicate


def print_res(t: tuple) -> None:
    (word, dup) = t
    s = ""              # based on prior (even or odd) category, print_res encodes into string and prints the results
    for letter in word:
        if letter in dup:
            s = s + ")"
        else:
            s = s + "("
    print(s)


if __name__ == '__main__':
    wrd = "(( @"
    pr1 = duplicate(wrd)
    print_res((wrd, pr1))
