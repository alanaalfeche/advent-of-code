import math

from data import load_day


def seat_id_calculator(data, min_num, max_num, min_char, max_char, df):
    _min = min_num
    _max = max_num

    for i, char in enumerate(data):
        if char == min_char:
            _max = math.floor((_max-_min) / 2) + _min
        elif char == max_char:
            _min = math.ceil((_max-_min) / 2) + _min
    return min(_min, _max) if df == min_char else max(_min, _max)

def get_seat_ids(boarding_passes):
    seat_ids = []
    for bp in boarding_passes:
        rows = bp[:6]
        deciding_factor = bp[6]
        cols = bp[7:]

        row = seat_id_calculator(rows, 0, 127, 'F', 'B', deciding_factor)
        col = seat_id_calculator(cols, 0, 7, 'L', 'R', deciding_factor)
        
        unique_seat_id = row * 8 + col
        seat_ids.append(unique_seat_id)
    return seat_ids

def find_my_seat(seat_ids):
    return [seat for seat in range(min(seat_ids), max(seat_ids)) if seat not in seat_ids][0]

boarding_passes = load_day(5)
seat_ids = get_seat_ids(boarding_passes)
# part a
print(max(seat_ids))
# part b
print(find_my_seat(seat_ids))