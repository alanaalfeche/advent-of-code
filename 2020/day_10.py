from data import load_day


data = load_day(10)

rating = {1: 0, 2: 0, 3: 0}
data = [int(x) for x in data]
data.sort()

print(data)
for i in range(len(data)-1):
    diff = data[i+1] - data[i]
    if diff <= 3:
        rating[diff] += 1
    print(i, rating)

# data[0] to account for the first adaptor
# +1 because my device built-in adapter is always 3 higher than the highest adapter
print((rating[1]+data[0]) * (rating[3]+1))