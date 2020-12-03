# Advent of Code 2020
# December 02, 2020
# https://adventofcode.com/2020/day/2

f = open("02/input")
count_p1 = 0
count_p2 = 0

for line in f.readlines():
    split = line.split()

    nums = split[0].split('-')
    char = split[1][0]
    pw = split[2]

    # PART 1
    char_count = pw.count(char)
    
    if (char_count >= int(nums[0]) and char_count <= int(nums[1])):
        count_p1 += 1

    # PART 2
    p1 = int(nums[0]) - 1
    p2 = int(nums[1]) - 1

    if ((pw[p1] == char and pw[p2] != char) or (pw[p1] != char and pw[p2] == char)):
        count_p2 += 1

print("PART 1:", count_p1)
print("PART 2:", count_p2)