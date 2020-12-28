from data import load_day


def navigate(data, waypoint=1+0j):
    # Credit goes to https://github.com/viliampucik/adventofcode/blob/master/2020/12.py
    actions = {'N': 0+1j, 'S': 0-1j, 'E': 1+0j, 'W': -1+0j}
    position = 0+0j
    waypoint_mode = waypoint != 1+0j

    for direction in data:
        action = direction[:1]
        value = int(direction[1:])
        if action == 'L':
            # 1j^1 = 0+1j  - N
            # 1j^2 = -1+0j - W
            # 1j^3 = 0-1j  - S
            # 1j^4 = 1+0j  - E
            waypoint *= pow(1j, value // 90)
        elif action == 'R':
            # -1j^1 = 0-1j  - S
            # -1j^2 = -1+0j - W
            # -1j^3 = 0+1j  - N
            # -1j^4 = 1+0j  - E
            waypoint *= pow(-1j, value // 90)
        elif action == 'F':
            # ex: position += 1+0j (default waypoint) * value
            position += waypoint * value
        elif waypoint_mode:
            # positioned above else to evaluate waypoint during a waypoint mode
            waypoint += actions[action] * value
        else:
            # ex: position += 0+1j (north) * value
            position += actions[action] * value
    return abs(position.real) + abs(position.imag)

instructions = load_day(12)
print(navigate(instructions))
print(navigate(instructions, 10+1j))