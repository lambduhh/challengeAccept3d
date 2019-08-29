# Leap years:
#
# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.

# This means that in the Gregorian calendar,
# the years 2000 and 2400 are leap years,
# while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.
#
# Task
# You are given the year, and you have to write a function to check if the year is leap or not.
#


def is_div_by_4(n):
    return n % 4 == 0


def is_div_by_100(n):
    return n % 100 == 0


def is_div_by_400(n):
    return n % 400 == 0


# store all data in a dictionary
def y_dict(year):
    ydata = {
        "year": year,
        "div-by-4?": is_div_by_4(year),
        "div-by-100?": is_div_by_100(year),
        "div-by-400?": is_div_by_400(year), }
    return ydata


# processes data from y_dict, performs logic and in the return statemnt creates new key:"leap-year?" w final answer
def calculate_leap_year(yd):
    if yd['div-by-4?'] and yd['div-by-400?']:
        leap = True
    elif yd['div-by-4?'] and yd['div-by-100?']:
        leap = False
    elif yd['div-by-4?']:
        leap = True
    else:
        leap = False
        # new y_dict with leap year status added, (dict unpacking)
    return {**yd, "leap-year?": leap}


def render_res(yd: dict) -> None:  
    print(yd['leap-year?'])
    return None


if __name__ == '__main__':
    pr = calculate_leap_year(y_dict(2300))
    render_res(pr)
