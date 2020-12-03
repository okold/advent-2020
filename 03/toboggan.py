# Advent of Code 2020
# December 03, 2020
# https://adventofcode.com/2020/day/3

# readlines_stripped
def readlines_stripped(filename):
    with open(filename) as f:
        lis = []
        line = f.readline().strip()
        while line:
            lis.append(line)
            line = f.readline().strip()
        return lis

# count_collisions
def count_collisions(array, dx, dy):
    x = 0
    count = 0
    for index, line in enumerate(array):
        if index % dy == 0: 
            if line[x] == '#':
                count += 1
            x = (x + dx) % len(line)
    return count

# PART 1
arr = readlines_stripped("03/input")
print("PART 1:", count_collisions(arr, 3, 1))

# PART 2
s1 = count_collisions(arr, 1, 1)
s2 = count_collisions(arr, 3, 1)
s3 = count_collisions(arr, 5, 1)
s4 = count_collisions(arr, 7, 1)
s5 = count_collisions(arr, 1, 2)

print("PART 2:", s1 * s2 * s3 * s4 * s5)