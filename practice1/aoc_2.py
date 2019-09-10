# (...)scan the likely candidate boxes again, counting the number that have an ID containing exactly two of any
# letter and then separately counting those with exactly three of any letter. You can multiply those
# two counts together to get a rudimentary checksum and compare it to what your device predicts.


from practice1.utils import convert_str_to_lst, read_file_by_line
from functools import reduce


# *the "folding" function that is made to pass to reduce
#  does not mutate data but instead uses "dictionary unpacking"
#  each time returning a new copy of a dictionary with new information

def next_occurrence(d: dict, key) -> dict:
    if key not in d:
        return {**d, key: 1}  # {a copy of the dict(d) with a key of 1}
    else:
        value = d[key]
        return {**d, key: value + 1}  # {a copy of the dict(d) with a new key +1 }


# pass in the boxid string and reduce will repeatedly "fold over"
# by applying the next_occurrence fn resulting in a dict
def occurrences(boxid: str) -> dict:
    return reduce(next_occurrence, boxid, {})


# turns the boxid str -> a dict with the data from occurrences nested inside
def augment_box_id(boxid: str) -> dict:
    return {'name': boxid,
            'occurrences': occurrences(boxid)}


# takes the list of strings and maps augment_box_id fn over each 'box' resulting in a dict for each box
def augment_ids(ids: list) -> list:
    return list(map(augment_box_id, ids))


def occurs_twice(d: dict) -> bool:
    if 2 in d['occurrences'].values():
        return True
    else:
        return False


def occurs_thrice(d: dict) -> bool:
    if 3 in d['occurrences'].values():
        return True
    else:
        return False


# dict_data = augment_ids(data)
# applies the filter fn to find which boxes have letters that occur 2 or 3 times and get a final checksum
def filter_by_occurrences(dict_data: dict) -> int:
    twice = list(filter(occurs_twice, dict_data))
    thrice = list(filter(occurs_thrice, dict_data))
    return len(twice) * len(thrice)


def render(int) -> None:
    print(int)
    return None


if __name__ == '__main__':
    ipt = read_file_by_line("txt_inputs/aoc2_input.txt")
    l = convert_str_to_lst(ipt)
    dict_data = augment_ids(l)
    fbo = filter_by_occurrences(dict_data)
    render(fbo)
