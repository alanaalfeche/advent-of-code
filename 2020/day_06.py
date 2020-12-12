any_yes = all_yes = 0

with open('2020/data/day_06') as f:
    for group in f.read().split('\n\n'):
        any_yes += len(set(group.replace('\n', '')))
        all_yes += len(set.intersection(
            *map(set, group.split())
        ))

print(any_yes)
print(all_yes)