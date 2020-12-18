# Advent of Code 2020 - Day 10
# December 17, 2020
# https://adventofcode.com/2020/day/10
import func

MIN_DIFF = 1
MAX_DIFF = 3

input = func.file_to_int_list("10/input")
input.append(0)                             # outlet joltage
input.append(max(input) + 3)                # built-in adapter joltage
input.sort()

# PART 1
one_jolt = 0
three_jolt = 0

for i, x in enumerate(input):
    if i < len(input) - 1:
        if input[i+1] - x == 1:
            one_jolt += 1
        else:
            if input[i+1] - x == 3:
                three_jolt += 1

print("PART 1:", one_jolt * three_jolt)

# PART 2
input.reverse()
dict = {}

for val in input:
    if val == max(input):
        dict[val] = 1
    else:
        dict[val] = 0
        for x in range(MIN_DIFF, MAX_DIFF + 1):
            if val + x in input:
                dict[val] += dict[val + x]
                
print("PART 2:", dict[0])