# Advent of Code 2020
# December 05, 2020
# https://adventofcode.com/2020/day/5
import func

# gen_all_ids()
def gen_all_ids():
    list = []
    for row in range(0, 127):
        for col in range(0, 8):
            list.append(row * 8 + col)
    return list

input = func.file_to_list("05/input")
max_id = 0
all_ids = gen_all_ids()

for line in input:
    max_row = 127
    min_row = 0
    max_col = 7
    min_col = 0
    
    for char in line:
        if char == 'F':
            max_row = func.get_mid(max_row, min_row)
        if char == 'B':
            min_row = func.get_mid(max_row, min_row)
        if char == 'L':
            max_col = func.get_mid(max_col, min_col)
        if char == 'R':
            min_col = func.get_mid(max_col, min_col)
    
    # PART 1
    seat_id = max_row * 8 + max_col
    if seat_id > max_id:
        max_id = seat_id

    #PART 2
    all_ids.remove(seat_id)

for i, val in enumerate(all_ids):
    if i > 0 and val < max_id:
        if all_ids[i-1] != (val - 1) and all_ids[i+1] != (val + 1):
            my_id = val
            break

print("PART 1:", max_id)
print("PART 1:", my_id)