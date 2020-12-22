from data import load_day


def get_adjacents(grid, row, col, row_size, col_size):
    adjacents = []
    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            if x == y == 0:
                continue
            if 0 <= row + x < row_size and 0 <= col + y < col_size:
                adjacents.append(grid[row + x][col + y])
    return adjacents


def get_occupied_seats(grid, row_size, col_size):
    new_grid = []
    for row in range(row_size):
        new_row = []

        for col in range(col_size):
            adjacents = get_adjacents(grid, row, col, row_size, col_size)

            if grid[row][col] == "L" and "#" not in adjacents:
                new_row += "#"
            elif grid[row][col] == "#" and adjacents.count("#") >= 4:
                new_row += "L"
            else:
                new_row += grid[row][col]

        new_grid.append(new_row)
    return new_grid


seating = load_day(11)
default_grid = []
for i in seating:
    row = []
    for char in i:
        row.append(char)
    default_grid.append(row)
row_size = len(default_grid)
col_size = len(default_grid[0])


# part a
process = True
while process:
    occupied_grid = get_occupied_seats(default_grid, row_size, col_size)

    if occupied_grid == default_grid:
        num = 0
        for x in occupied_grid:
            num += x.count('#')
        print(num)
        process = False

    default_grid = occupied_grid
