import itertools

from data import load_day


def group_answers(answers):
    return [list(''.join(g)) for k, g in itertools.groupby(answers, key=lambda x: x == '')]

def count_yes(group_answers):
    custom_yes_count = 0
    for answer in group_answers:
        if answer: custom_yes_count += len(set(answer))
    return custom_yes_count

custom_answers = load_day(6)
group_answers = group_answers(custom_answers)
# part a
print(count_yes(group_answers))
