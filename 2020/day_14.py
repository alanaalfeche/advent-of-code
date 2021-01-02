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
        value &= and_mask
        value |= or_mask
        mem[int(l[4:-1])] = value

print(sum(mem.values()))