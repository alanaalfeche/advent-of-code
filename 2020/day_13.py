from data import load_day


def calculate_min_wait_time(ts, buses):
    wait_times = [bus - ts%bus for bus in buses]
    bus_index = wait_times.index(min(wait_times))
    return buses[bus_index]*min(wait_times)


def calculate_subsequent_departures(buses):
    ''' We need to find a number such that it's divisible by the first bus, then second bus + index, and so on.
    Take 7, 13, x, x, 59... for an example. At 77, 77 % 7 = 0, and 78 % 13 = 0.
    So, the n is where n % 7 = 0, (n + 1) % 13 = 0, and (n + 4) % 59 = 0.

    Note that all bus IDs are prime numbers so we can just iterate with the LCM until it meets our codition.
    The maximum solution is the product of all numbers. 
    '''
    time, step = 0, 1

    for delta, bus in buses.items():
        while (time + delta) % bus: # if not divisible, enter while loop; if divisible, we found the LCM, exit while loop
            time += step # add step until time + delta is divisible by bus ID
        step *= bus # lcm of previous numbers is added to step to ensure that the next number will be divisible by previous AND current
    return time


data = load_day(13)
ts = int(data[0])
buses = {
    i: int(bus) 
    for i, bus in enumerate(data[1].split(',')) 
    if bus != 'x'
}

print(calculate_min_wait_time(ts, list(buses.values())))
print(calculate_subsequent_departures(buses))