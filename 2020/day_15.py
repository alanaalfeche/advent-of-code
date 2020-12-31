from data import load_day


def memory_game(seen, last, limit):
    for i in range(len(seen), limit):
        # tmp = last
        # last = i - seen.get(last, i)
        # seen[tmp] = i        
        seen[last], last = i, i - seen.get(last, i)
    return last


data = load_day(15)
data = [int(ele) for ele in data[0].split(',')]
last = data[-1]
seen = {num: turn+1 for turn, num in enumerate(data)}
# part one
print(memory_game(seen.copy(), last, 2020))
# part two -- takes 12 seconds
print(memory_game(seen.copy(), last, 30000000))
