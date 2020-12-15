import re
from collections import defaultdict

from data import load_day


instruction = defaultdict(dict)
def parse_data(boot_code):
    for index, line in enumerate(boot_code):
        operation, argument = line.split()
        instruction[index][operation] = argument

def terminate():
    visited = []
    accumulator, pointer = 0, 0
    while pointer not in visited and pointer < len(instruction):
        visited.append(pointer)

        [(op, args)] = instruction[pointer].items()
        step = int(args)

        if op == 'acc':
            accumulator += step
            pointer += 1
        elif op == 'jmp':
            pointer += step
        elif op == 'nop':
            pointer += 1
    return accumulator
 
boot_code = load_day(8)
parse_data(boot_code)
# part a
print(terminate())