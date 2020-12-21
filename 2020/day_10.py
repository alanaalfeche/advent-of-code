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
    pass

data = load_day(10)
data = [int(x) for x in data]
# part a
print(multiply_jolt_differences(data))
# part b
print(get_total_paths(data))