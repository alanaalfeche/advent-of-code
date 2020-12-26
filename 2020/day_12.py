from data import load_day


def navigate(data, waypoint=1+0j):
    # Credit goes to https://github.com/viliampucik/adventofcode/blob/master/2020/12.py
    actions = {'N': 1j, 'S': -1j, 'E': 1, 'W': -1}
    position = 0+0j
    waypoint_mode = waypoint != 1+0j

    for direction in data:
        action = direction[:1]
        value = int(direction[1:])
        if action == 'L':
            waypoint *= pow(1j, value // 90)
        elif action == 'R':
            waypoint *= pow(-1j, value // 90)
        elif action == 'F':
            position += waypoint * value
        elif waypoint_mode:
            waypoint += actions[action] * value
        else:
            position += actions[action] * value

    return abs(position.real) + abs(position.imag)

instructions = load_day(12)
print(navigate(instructions))
print(navigate(instructions, 10+1j))