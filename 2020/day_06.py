from itertools import groupby

from data import load_day


def group_answers(custom_answers):
    return [list(g) for k, g in groupby(custom_answers, key=lambda x: x != '') if k]

def count_any_yes(group_answers):
    any_yes = 0
    for group in group_answers:
        any_yes += len(set(''.join(group)))
    return any_yes

def count_all_yes(group_answers):
    all_yes = 0
    for group in group_answers:
        if len(group) == 1:
            all_yes += len(group[0])
        else:
            for answer in group[0]:
                if all(answer in person for person in group[1:]):
                    all_yes += 1
    return all_yes

custom_answers = load_day(6)
parsed_data = group_answers(custom_answers)
# part a
print(count_any_yes(parsed_data))
# part b
print(count_all_yes(parsed_data))
