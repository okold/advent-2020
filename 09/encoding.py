# Advent of Code 2020 - Day 9
# December 14, 2020
# https://adventofcode.com/2020/day/7
import func
import re
import time

P_SIZE = 25  # preamble size

# is_sum(num)
# returns True if num can be created as a sum of two unique values in the 
# preamble
def is_sum(num):
    for x in preamble:
        for y in preamble:
            if x + y == num and x != y:
                return True
    return False

# PART 1
input = func.file_to_int_list("09/input")
preamble = []
invalid_num = 0

for i in range(0, P_SIZE):
    preamble.append(input[i])

next = P_SIZE
while next < len(input):
    num = input[next]
    if is_sum(num):
        del preamble[0]
        preamble.append(input[next])
        next += 1
    else:
        invalid_num = num
        print("PART 1:", num)
        break

# PART 2
for i, x in enumerate(input):
    sum_list = []
    current_sum = 0
    for j in range(i, len(input)):
        sum_list.append(input[j])
        current_sum = sum(sum_list)
        if current_sum == invalid_num:
            print("PART 2:", min(sum_list) + max(sum_list))
            break
    if current_sum == invalid_num:
        break