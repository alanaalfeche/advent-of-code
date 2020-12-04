def parse_data(input_file):
    with open(input_file) as f:
        lines = f.read().splitlines()

    return list(map(int, lines))
