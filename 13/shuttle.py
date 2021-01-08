# Advent of Code 2020 - Day 13
# December 13, 2020
# https://adventofcode.com/2020/day/13
import helper
import itertools
import sys
import time
from helper import *

input = file_to_list("13/input")

################################################################################
# PART 1

estimate = int(input[0])
earliest_bus = 0
bus_time = sys.maxsize
bus_list = str_to_int_list(input[1], ',')

for bus in bus_list:
    t = bus
    while t < estimate:
        t += bus
        
    if t < bus_time:
            bus_time = t
            earliest_bus = bus

wait_time = bus_time - estimate
print("PART 1:", earliest_bus * wait_time)

################################################################################
# PART 2
# INCOMPLETE. WORKS, BUT IT'S SO INEFFICIENT IT WON'T REACH A SOLUTION.

# calculates the needed differences between the values in bus_list
steps = {}
last_val = 0

for val in input[1].split(','):
    if val.isdigit():
        last_val = int(val)
        steps[last_val] = 1
    else:
        steps[last_val] += 1

# tests every multiple of the first bus, to see if it matches the sequence

def test_forwards(val, bus_index):
    if bus_index == len(bus_list) - 1:
        return (True, val)
    else:
        next_val = val + steps[bus_list[bus_index]]
        if next_val % bus_list[bus_index + 1] == 0:
            return test(next_val, bus_index + 1)
        else:
            return (False, 0)

def test_backwards(val, bus_index):
    if bus_index == 0:
        return (True, val)
    else:
        prev_val = val - steps[bus_list[bus_index - 1]]
        if prev_val % bus_list[bus_index - 1] == 0:
            return test_backwards(prev_val, bus_index - 1)
        else:
            return (False, 0)

def test(val, bus_index):
    back = test_backwards(val, bus_index) 
    front = test_forwards(val, bus_index)
    if back[0] and front[0]:
        return (True, back[1])
    else:
        return (False, 0)

# # testing forwards
# done = False
# start = int(100000000000000 / bus_list[0]) * bus_list[0]
# start_time = time.perf_counter()
# while not(done):
#     start += bus_list[0]
#     result = test_forwards(start, 0)
#     done = result[0]
# end_time = time.perf_counter()
# print("testing forwards:", bus_list[0], "-", bus_list[len(bus_list) - 1])
# print(result[1], "(", end_time - start_time, ")")

# # testing backwards
# done = False
# end = 0
# start_time = time.perf_counter()
# while not(done):
#     end += bus_list[len(bus_list) - 1]
#     result = test_backwards(end, len(bus_list) - 1)
#     done = result[0]
# end_time = time.perf_counter()
# print("testing backwards:", bus_list[len(bus_list) - 1], "-", bus_list[0])
# print(result[1], "(", end_time - start_time, ")")

# testing both
done = False
max_bus = max(bus_list)
#start = 0
start = 100000000000000
start_index = bus_list.index(max_bus)
start_time = time.perf_counter()
while not(done):
    start += max_bus
    print(time.perf_counter(), "|", start)
    result = test(start, start_index)
    done = result[0]
end_time = time.perf_counter()
print("testing from max:", max_bus)
print(result[1], "(", end_time - start_time, ")")

