# Advent of Code 2020 - Day 12
# December 12, 2020
# https://adventofcode.com/2020/day/12
import helper
from helper import *

input = file_to_list("12/input")

DIRECTIONS = ['E', 'N', 'W', 'S']

dir_angle = {
    'E' : 0,
    'N' : 90,
    'W' : 180,
    'S' : 270,
    0 : 'E',
    90 : 'N',
    180 : 'W',
    270 : 'S'
}

def move(direction, amount, coords):
    if direction == 'E':
        return (coords[0] + amount, coords[1])
    if direction == 'N':
        return (coords[0], coords[1] + amount)
    if direction == 'W':
        return (coords[0] - amount, coords[1])
    if direction == 'S':
        return (coords[0], coords[1] - amount)
    return coords

################################################################################
# PART 1

def turn_ship(direction, angle):
    curr_angle = dir_angle[direction]
    new_angle = sum_angles(curr_angle, angle)
    return dir_angle[new_angle]

direction = 'E'                               
coords = (0, 0) # (x, y)

for line in input:
    action = line[0]
    amount = int(line[1:])

    if action == 'F':
        coords = move(direction, amount, coords)
    else:
        if action == 'L':
            direction = turn_ship(direction, amount)
        else:
            if action == 'R':
                direction = turn_ship(direction, 0 - amount)
            else:
                coords = move(action, amount, coords)

print("PART 1:", abs(coords[0]) + abs(coords[1]))

################################################################################
# PART 2

def move_to_waypoint(ship, waypoint, num_times):
    disp = (waypoint[0] * num_times, waypoint[1] * num_times) # displacement
    return (ship[0] + disp[0], ship[1] + disp[1])

def rotate_waypoint(angle, dir, coords):
    angle = sum_angles(angle, 0) # this is a dumb way to reset the angle but eh

    if (angle == 90 and dir == 'L') or (angle == 270 and dir == 'R'): 
        return (-1 * coords[1], coords[0])

    if (angle == 90 and dir == 'R') or (angle == 270 and dir == 'L'): 
        return (coords[1], -1 * coords[0])
    
    if angle == 180:
        return (-1 * coords[0], -1 * coords[1])

    return coords
                        
ship = (0, 0)       # (x, y)
waypoint = (10, 1)

for line in input:
    action = line[0]
    amount = int(line[1:])

    if action == 'F':
        ship = move_to_waypoint(ship, waypoint, amount)
    if action == 'L' or 'R':
        waypoint = rotate_waypoint(amount, action, waypoint)
    if action in DIRECTIONS:
        waypoint = move(action, amount, waypoint)

print("PART 2:", abs(ship[0]) + abs(ship[1]))