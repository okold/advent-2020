# Advent of Code 2020 - Day 8
# December 14, 2020
# https://adventofcode.com/2020/day/8
import func
import bootcomp
import re

# PART 1
# looper_scooper(comp, input)
# snoops for loops, returning the value of
# the accumulator at the first repeated index 
def looper_scooper(comp, input):
    comp.load(input)
    done = False
    sequence = []
    while not(done):
        if comp.halted:
            done = True
        else:
            if sequence.count(comp.current) > 0:
                done = True
            else:
                sequence.append(comp.current)
                comp.step()
    return (comp.accumulator, comp.halted)

input = func.file_to_list("08/input")
comp = bootcomp.BootComp()
p1 = looper_scooper(comp, input)[0]

print("PART 1:", p1)

# PART 2
comp.reset()
nop_indices = []
jmp_indices = []
nop_re = re.compile("\Anop")
jmp_re = re.compile("\Ajmp")

# finds all the nops and jmps
for index, line in enumerate(input):
    if nop_re.match(line):
        nop_indices.append(index)
    if jmp_re.match(line):
        jmp_indices.append(index)

# swaps all the nops one by one
if not(comp.halted):
    for index in nop_indices:
        mod_input = []
        i = 0
        for line in input:
            if i == index:
                split = input[index].split(' ')
                mod_input.append("jmp " + split[1])
            else:
                mod_input.append(line)
            i += 1
        comp.reset()
        result = looper_scooper(comp, mod_input)[0]
        if comp.halted:
            print("PART 2:", result)
            break

# swaps all the jmps one by one
if not(comp.halted):
    for index in jmp_indices:
        mod_input = []
        i = 0
        for line in input:
            if i == index:
                split = input[index].split(' ')
                mod_input.append("nop " + split[1])
            else:
                mod_input.append(line)
            i += 1
        comp.reset()
        result = looper_scooper(comp, mod_input)[0]
        if comp.halted:
            print("PART 2:", result)
            break