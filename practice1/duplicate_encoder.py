def duplicate(word):
    single = []
    dup = []
    letters = list(word)
    for letter in letters:
        if letter not in single:
            single.append(letter)
        else:
            dup.append(letter)

    return dup


def print_res(t: tuple) -> None:
    (word, dup) = t
    s = ""
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
