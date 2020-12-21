from collections import defaultdict
from data import load_day


def multiply_jolt_differences(data):
    rating = defaultdict(int)

    data.insert(0, 0)
    data.sort()
    for i in range(len(data)-1):
        diff = data[i+1] - data[i]
        if diff <= 3:
            rating[diff] += 1

    return rating[1] * (rating[3]+1) # built-in adapter is always 3 higher than the highest adapter


def get_total_paths(data):
    paths = defaultdict(int)
    paths[0] = 1

    for adapter in sorted(data):
        for diff in range(1, 4):
            next = adapter + diff
            if next in data:
                paths[next] += paths[adapter]
    
    x = max(paths, key=int)
    return paths[x]


data = load_day(10)
data = [int(x) for x in data]
# part a
print(multiply_jolt_differences(data))
# part b
print(get_total_paths(data))
