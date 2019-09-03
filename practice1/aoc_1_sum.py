# Below the message, the device shows a sequence of changes in frequency (your puzzle input).
# A value like +6 means the current frequency increases by 6;
# a value like -3 means the current frequency decreases by 3.
#
# For example, if the device displays frequency changes of [+1, -2, +3, +1,]
# then starting from a frequency of zero, the following changes would occur:
#
# Current frequency  0, change of +1; resulting frequency  1.
# Current frequency  1, change of -2; resulting frequency -1.
# Current frequency -1, change of +3; resulting frequency  2.
# Current frequency  2, change of +1; resulting frequency  3.

# Part I
# Starting with a frequency of zero,
# what is the resulting frequency after all of the changes in frequency have been applied?

# Part II- You notice that the device repeats the same frequency change list over and over.
# To calibrate the device, you need to find the first frequency it reaches twice.Note that your device
# might need to repeat its list of frequency changes many times before a duplicate frequency is found,
# and that duplicates might be found while in the middle of processing the list.

from practice1.utils import read_file_by_line


#  first thing I do is create a data structure (a dict) with all the information I would like to interact with
def freq_changes(ipt):
    freqs = {"current-freq": "0",
             "change-of": "0",
             "result": [0],  # "result" will be a cumulative sum list of results
             "counts": {},
             }
    for number in ipt:  # a fancy way of getting a cumulative sum for all the data
        freqs["current-freq"] = freqs["result"][-1]
        freqs["change-of"] = number
        freqs["result"].append(freqs["current-freq"] + freqs["change-of"])
    # the advantage of this is that print(freqs) properly illustrates the data through each change
    # this is handy for testing against the example shown above = Part I completed
    for num in freqs["result"]:
        # the goal of the next for loop is to loop through the list of cumulative sums (AKA freqs["results"])
        # to find a duplicate number
        if num not in freqs["counts"]:
            freqs["counts"][num] = 0
            freqs["dups"] = False
        freqs["counts"][num] += 1
        # when it finds a duplicate number, it changes the value of freqs["dups"] and stores the number there
        if freqs["counts"][num] >= 2:
            freqs["dups"] = num
            return freqs
    return freqs


# since the original challenge requires looping through the cumulative sum multiple times before a dup is found,
# I need a fn to repeat the list
def repeat_list(n, xs):
    return xs * n


def render(d: dict) -> None:
    print(d["result"][-1])  # prints the cumulative total after one time around
    d = freq_changes(repeat_list(1000, ipt)) # repeats the whole process many times so a duplicate can be found
    if d["dups"] is not False: # when freq["dups"] finally finds/stores a duplicate number, print the dup
        print(d["dups"])
    return None


if __name__ == '__main__':
    ipt = read_file_by_line("txt_inputs/aoc1_input.txt")
    ipt = list(map(int, ipt)) # turns ipt into a list of numbers that can be looped through
    pr = freq_changes(ipt)
    render(pr)
