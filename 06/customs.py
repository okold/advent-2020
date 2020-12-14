# Advent of Code 2020 - Day 6
# December 14, 2020
# https://adventofcode.com/2020/day/6
import func

input = func.file_to_list("06/input")

# PART 1
charlist = []
total = 0

for line in input:
    if line == '':
        charlist = []
    else:
        for char in line:
            if charlist.count(char) == 0:
                charlist.append(char)
                total += 1

print("PART 1:", total)

# PART 2
input.append('') # so that the final group is processed
charlist = []
group_size = 0
total = 0

for line in input:
    if line == '':
        charset = list(set(charlist))
        for char in charset:
            count = charlist.count(char)
            if count == group_size:
                total += 1
        charlist = []
        group_size = 0
    else:
        group_size += 1
        for char in line:
            charlist.append(char)

print("PART 2:", total)