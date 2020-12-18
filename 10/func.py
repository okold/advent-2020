# func.py
# Olga Koldachenko
#
# file_to_list(filename)    - Creates a pre-stripped list of strings
# file_to_int_list(filename)- Creates list of integers from a file
# reset(list)               - Sets all the values in a list to 0
# negate(list, index)       - Swaps 0 and 1 at the given index
# get_mid(max, min)         - Returns the midpoint between two ints as an int

# file_to_list(filename)
# Takes the path of a text file, and returns a list containing each line, 
# pre-stripped.
def file_to_list(filename):
    with open(filename) as f:
        raw = f.readlines()
        stripped = []
        for line in raw:
            stripped.append(line.strip())
        return stripped

# file_to_int_list(filename)
# Takes the path of a text file which contains an integer in each line, and
# returns a list of the integers.
def file_to_int_list(filename):
    with open(filename) as f:
        raw = f.readlines()
        stripped = []
        for line in raw:
            stripped.append(int(line.strip()))
        return stripped

# reset(list)
# Sets everything in the given list to 0.
def reset(list):
    for index, x in enumerate(list):
        list[index] = 0

# negate(list, index)
# Swaps a 0 with a 1 and vice-versa within a given list and index.
def negate(list, index):
    if list[index] == 0:
        list[index] = 1
    else:
        if list[index] == 1:
            list[index] = 0

# get_mid(max, min)
# Returns the middle value between two numbers as an integer.
def get_mid(max, min):
    mid = max - ((max - min) / 2)
    return int(mid)