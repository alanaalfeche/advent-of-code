from data import load_day


def calculate_min_wait_time(ts, buses):
    wait_times = [bus - ts%bus for bus in buses]
    bus_index = wait_times.index(min(wait_times))
    return buses[bus_index]*min(wait_times)


data = load_day(13)
ts = int(data[0])
buses = [int(bus) for bus in data[1].split(',') if bus != 'x']
print(calculate_min_wait_time(ts, buses))