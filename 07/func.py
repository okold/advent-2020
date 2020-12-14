# func.py
# Olga Koldachenko
# Contains various methods regarding lists and math.
#
# file_to_list(filename)    - Creates a pre-stripped list of strings from a file 
# reset(list)               - Sets all the values in a list to 0
# negate(list, index)       - Swaps 0s and 1s at the given index
# get_mid(max, min)         - Returns the midpoint between two numbers as an integer

# file_to_list(filename)
# Takes the path of a text file, and returns a
# list containing each line, pre-stripped.
def file_to_list(filename):
    with open(filename) as f:
        raw = f.readlines()
        stripped = []
        for line in raw:
            stripped.append(line.strip())
        return stripped

# reset(list)
# Sets everything in the given list to 0.
def reset(list):
    for index, x in enumerate(list):
        list[index] = 0

# negate(list, index)
# Swaps a 0 with a 1 and vice-versa within a
# given list and index.
def negate(list, index):
    if list[index] == 0:
        list[index] = 1
    else:
        if list[index] == 1:
            list[index] = 0

# get_mid(max, min)
# Returns the middle value between two
# numbers as an integer.
def get_mid(max, min):
    mid = max - ((max - min) / 2)
    return int(mid)