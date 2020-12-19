# helper.py
# Version 0.12
# Various IO/list/matrix functions, developed during Advent of Code 2020.
# Olga Koldachenko
#
# file_to_list(filename)            - Creates a pre-stripped list of strings
# file_to_int_list(filename)        - Creates list of integers from a file
# file_to_char_matrix(filename)     - Creates a 2D array of chars from a file
# reset(list)                       - Sets all the values in a list to 0
# negate(list, index)               - Swaps 0 and 1 at the given index
# get_mid(max, min)                 - Returns the midpoint between two ints
# equal_matrices(a, b)              - True if the given 2D arrays are equal
#                                     NOTE: MUST BE OF EQUAL SIZE, DOES NO
#                                           CHECKING FOR THAT AT THE MOMENT!!!
# sum_angles(angle, mod)            - Sums two integer angles, 
#                                     returning a positive angle
################################################################################

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

# file_to_char_matrix(filename)
# Creates a 2D array of characters from a text file.
def file_to_char_matrix(filename):
    with open(filename) as f:
        raw = f.readlines()
        matrix = []
        for i, line in enumerate(raw):
            if len(line) > 0:
                matrix.append([])
            for char in line:
                if char != '\n':
                    matrix[i].append(char)
        return matrix

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

# equal_matrices(a, b)
# True if the given 2D arrays are equal
def equal_matrices(a, b):
    for y in range(0, len(a)):
        for x in range(0, len(a[y])):
            if a[y][x] != b[y][x]:
                return False
    return True

# sum_angles(angle, mod)
# Sums two integer angles
def sum_angles(angle, mod):
    new_angle = (angle + mod) % 360
    while new_angle < 0:
        new_angle = 360 - new_angle
    return new_angle