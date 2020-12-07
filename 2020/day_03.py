from data import load_day


def count_trees(lines, rise, run):
    line_size = len(lines[0])
    x, tree_count = 0, 0
    for line in lines[::rise]:
        tree_count += line[x] == '#'
        x = (x + run) % line_size
    return tree_count

lines = load_day(3)
# part a
print(count_trees(lines, 1, 3)) # 276
# part b
print(count_trees(lines, 1, 1) * \
      count_trees(lines, 1, 3) * \
      count_trees(lines, 1, 5) * \
      count_trees(lines, 1, 7) * \
      count_trees(lines, 2, 1))
