# Source: https://github.com/sijmn/aoc2020/blob/master/python/day14.py
from data import load_day


data = load_day(14)
mem = {}
for line in data:
    l, r = line.split(' = ')
    if l == 'mask':
        and_mask = int(r.replace('X', '1'), base=2)
        or_mask = int(r.replace('X', '0'), base=2)
    else:
        value = int(r)
        value &= and_mask # each bit of output is 1 if x AND y is 1, otherwise it's 0
        value |= or_mask # each bit of output is 0 if x AND y is 0, otheriwse it's 1
        mem[int(l[4:-1])] = value

print(sum(mem.values()))