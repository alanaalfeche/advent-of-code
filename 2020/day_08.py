import re
from collections import defaultdict

from data import load_day


instruction = defaultdict(dict)
def parse_data(boot_code):
    for index, line in enumerate(boot_code):
        operation, argument = line.split()
        instruction[index][operation] = argument

def terminate(i=None):
    visited = []
    accumulator, pointer = 0, 0
    while pointer not in visited and pointer < len(instruction):
        visited.append(pointer)

        [(op, args)] = instruction[pointer].items()
        step = int(args)
        
        if pointer == i:
            op = 'nop' if op == 'jmp' else 'jmp'

        if op == 'acc':
            accumulator += step
            pointer += 1
        elif op == 'jmp':
            pointer += step
        elif op == 'nop':
            pointer += 1
    return visited, pointer, accumulator


boot_code = load_day(8)
parse_data(boot_code)
# part a
visited, _, accumulator = terminate()
print(accumulator)
# part b
for i in visited:
    [(op, args)] = instruction[i].items()
    if op in ('nop', 'jmp'):
        _, j, accumulator = terminate(i)
        if j >= len(instruction):
            print(accumulator)
            break