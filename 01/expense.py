# Advent of Code 2020
# December 01, 2020
# https://adventofcode.com/2020/day/1

# read_integers
# https://codereview.stackexchange.com/questions/12443/reading-ints-line-from-a-file-in-python/12449
def read_integers(filename):
    with open(filename) as f:
        return [int(x) for x in f]

# PART 1
nums = read_integers("input.txt")
done = False

for x in nums:
    if done:
        break
    for y in nums:
        if done:
            break
        if x + y == 2020:
            done = True
            print("PART 1: ")
            print(x * y)

# PART 2
done = False
for x in nums:
    if done:
        break
    for y in nums:
        if done:
            break
        for z in nums:
            if done:
                break
            if x + y + z == 2020:
                done = True
                print("PART 2: ")
                print(x * y * z)