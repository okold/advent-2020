# Advent of Code 2020 - Day 11
# December 18, 2020
# https://adventofcode.com/2020/day/11
import func
import copy

input = func.file_to_char_matrix("11/input")
current = copy.copy(input)
WIDTH = len(input[0])
HEIGHT = len(input)

# PART 1
def num_adjacent(y, x):
    num = 0
    for x2 in [-1, 0, 1]:
        x3 = x + x2
        if x3 >= 0 and x3 < WIDTH:
            for y2 in [-1, 0, 1]:
                if not(x2 == 0 and y2 == 0):
                    y3 = y + y2
                    if y3 >= 0 and y3 < HEIGHT:
                        if current[y3][x3] == '#':
                            num += 1
    return num

def update():
    num_occupied = 0
    next = []
    for i, y in enumerate(range(0, HEIGHT)):
        next.append([])
        for x in range(0, WIDTH):
            if current[y][x] == 'L' and num_adjacent(y, x) == 0:
                next[i].append('#')
                num_occupied += 1
            else:
                if current[y][x] == '#' and num_adjacent(y, x) >= 4:
                    next[i].append('L')
                else:
                    next[i].append(current[y][x])
                    if current[y][x] == '#':
                        num_occupied += 1
    return (next, num_occupied)

done = False
while not(done):
    double = update()
    new = double[0]
    if func.equal_matrices(current, new):
        done = True
        answer = double[1]
    else:
        current = new
    
print("PART 1:", answer)

# PART 2
def num_visible(y, x):
    num = 0
    for x2 in [-1, 0, 1]:
        for y2 in [-1, 0, 1]:
            if not(x2 == 0 and y2 == 0):
                if visible_seat(y, x, x2, y2):
                    num += 1
    return num

def visible_seat(y, x, y_dir, x_dir):
    y_temp = y
    x_temp = x
    while True:
        y_temp += y_dir
        x_temp += x_dir
        if (y_temp == -1 or x_temp == -1 
            or y_temp == HEIGHT or x_temp == WIDTH
            or current[y_temp][x_temp] == 'L'):
            return False
        if current[y_temp][x_temp] == '#':
            return True

def update_v2():
    num_occupied = 0
    next = []
    for i, y in enumerate(range(0, HEIGHT)):
        next.append([])
        for x in range(0, WIDTH):
            if current[y][x] == 'L' and num_visible(y, x) == 0:
                next[i].append('#')
                num_occupied += 1
            else:
                if current[y][x] == '#' and num_visible(y, x) >= 5:
                    next[i].append('L')
                else:
                    next[i].append(current[y][x])
                    if current[y][x] == '#':
                        num_occupied += 1
    return (next, num_occupied)

current = copy.copy(input)
done = False
while not(done):
    double = update_v2()
    new = double[0]
    if func.equal_matrices(current, new):
        done = True
        answer = double[1]
    else:
        current = new
    
print("PART 1:", answer)