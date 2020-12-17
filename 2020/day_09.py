from collections import deque
from data import load_day


def find_invalid_number(data, preamble_length):
    preamble = deque(data[:preamble_length])
    invalid = None

    for i in data[preamble_length:]:
        seen = set()
        for j in preamble:
            if i - j in seen:
                preamble.popleft()
                preamble.append(i)
                break
            seen.add(j)
        else:
            invalid = i
            break

    return invalid


data = [int(x) for x in load_day(9)]
# part a
invalid = find_invalid_number(data, preamble_length=5)
print(invalid)
# part b
l = r = total = 0
while total != invalid:
    while total < invalid:
        total += data[r]
        r += 1
    while total > invalid:
        total -= data[l]
        l += 1
print(min(data[l:r]) + max(data[l:r]))