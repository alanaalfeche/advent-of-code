def load_day(n):
    input_file = f'2020/data/day_{n:02}'
    with open(input_file) as f:
        lines = f.read().splitlines()
    return lines
