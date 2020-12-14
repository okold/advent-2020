# Advent of Code 2020 - Day 4
# December 04, 2020
# https://adventofcode.com/2020/day/4
import listmod
import re

# validate(list, index)
# swaps a 0 with a 1 and a 1 with a -1, to validate
# the number of instances of each entry type.
def validate(list, index):
    if list[index] == 0:
        list[index] = 1
    else:
        if list[index] == 1:
            list[index] = -1

VALID_ECL = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
check = [0, 0, 0, 0, 0, 0, 0]   # byr, iyr, eyr, hgt, hcl, ecl, pid
inp = listmod.file_to_list("04/input")
valid_passports = 0

# PART 1
for line in inp:
    if line == '':
        if check == [1, 1, 1, 1, 1, 1, 1]:
            valid_passports += 1
        listmod.reset(check)
    else:
        if "byr:" in line:
            validate(check, 0)
        if "iyr:" in line:
            validate(check, 1)
        if "eyr:" in line:
            validate(check, 2)
        if "hgt:" in line:
            validate(check, 3)
        if "hcl:" in line:
            validate(check, 4)
        if "ecl:" in line:
            validate(check, 5)
        if "pid:" in line:
            validate(check, 6)
            
print("PART 1:", valid_passports)

# PART 2
listmod.reset(check)
valid_passports = 0
ecl_re = re.compile("^#([a-z]|[0-9]){6}$")

for line in inp:
    if line == '':
        if check == [1, 1, 1, 1, 1, 1, 1]:
            valid_passports += 1
        listmod.reset(check)
    else:
        split = line.split(' ')
        for sub in split:
            data = sub.split(":")[1]
            if "byr:" in sub:
                if int(data) >= 1920 and int(data) <= 2002:
                    validate(check, 0)
            if "iyr:" in sub:
                if int(data) >= 2010 and int(data) <= 2020:
                    validate(check, 1)
            if "eyr:" in sub:
                if int(data) >= 2020 and int(data) <= 2030:
                    validate(check, 2)
            if "hgt:" in sub:
                if data.endswith("in"):
                    if int(data[0:-2]) >= 59 and int(data[0:-2]) <= 76:
                        validate(check, 3)
                if data.endswith("cm"):
                    if int(data[0:-2]) >= 150 and int(data[0:-2]) <= 193:
                        validate(check, 3)
            if "hcl:" in sub:
                if ecl_re.match(data):
                    validate(check, 4)
            if "ecl:" in sub:
                if data in VALID_ECL:
                    validate(check, 5)
            if "pid:" in sub:
                if data.isdigit() and len(data) == 9:
                    validate(check, 6)
            
print("PART 2:", valid_passports)
