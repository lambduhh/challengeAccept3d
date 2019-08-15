# Complete the solution so that it reverses all of the words
# within the string passed in.
#
# Example:
#
# reverseWords("The greatest victory is that which requires no battle")
# // should return "battle no requires which that is victory greatest The"


def reverse_phrase(quote):
    l = str.split(quote)
    nl = []
    for words in reversed(l):
        nl.append(words)
    return ' '.join(nl)


def print_results(s):
    print(s)


if __name__ == '__main__':
    l = "hello from the other side"

    rp = reverse_phrase(l)
    print_results(rp)
