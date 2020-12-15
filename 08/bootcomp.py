# bootcomp.py
# Boot Computer - Day 8 Edition - Advent of Code 2020 
# Olga Koldachenko
#
# OPERATIONS:
#   - nop x | no operation, ignores the argument, proceeds to the next position
#   - acc x | modifies the accumulator value by x, proceeds to the next position
#   - jmp x | modifies the current position by x
#
# METHODS:
#   - BootComp()    | constructor
#   - load(code)    | deep copies a script into memory
#   - reset()       | sets the position and accumulator to 0
#   - step()        | computes the next instruction
#   - print_state() | prints the current state in the format:
#                     position  |   accumulator | instruction at position

class BootComp:
    def __init__(self):
        self.memory = []
        self.current = int(0)
        self.accumulator = int(0)
        self.halted = False
    
    # load(code)
    # deep copies a program into the machine's memory
    def load(self, code):
        self.memory = []
        
        for line in code:
            self.memory.append(line)

    # reset()
    # resets the current position and the
    # accumulator value, but does not wipe
    # the memory
    def reset(self):
        self.current = int(0)
        self.accumulator = int(0)
        self.halted = False

    # step()
    # processes the current instruction
    def step(self):
        if not(self.halted):
            if self.current >= len(self.memory):
                self.halted = True
            else:
                line = self.memory[self.current].split(' ')
                op = line[0]
                arg = int(line[1])

                if op == "nop":
                    self.current += 1
                    
                if op == "jmp":
                    self.current += arg

                if op == "acc":
                    self.accumulator += arg
                    self.current += 1

    # print_state()
    # prints the current instruction to the terminal,
    # in order of the memory location, accumulator value,
    # and state of the memory at the current position
    def print_state(self):
        if self.halted:
            print(self.current, '\t', self.accumulator, "\t DONE!")
        else:
            if self.current < len(self.memory):
                print(self.current, '\t', self.accumulator, '\t', self.memory[self.current])
            else:
                print(self.current, '\t', self.accumulator, '\t', "OUT OF BOUNDS")
