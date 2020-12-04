from collections import namedtuple

from data.input import load


def parse(lines):
    Password = namedtuple('Password', ['min', 'max', 'letter', 'password'])
    res = []
    for l in lines:
        policy, letter, password = l.split()
        _min, _max = policy.split('-')
        _letter = letter[0]
        res.append(Password(int(_min), int(_max), _letter, password))
    return res

def password_range_policy_validator(content):
    count = 0
    for ele in content:
        freq = ele.password.count(ele.letter)
        if ele.min <= freq <= ele.max: count += 1
    print(count)

def password_position_policy_validator(content):
    count = 0
    for ele in content:
        try:
            # ^ XOR operator sets bit to 1 if one of two bits is 1
            if (ele.password[ele.min-1] == ele.letter) ^ \
               (ele.password[ele.max-1] == ele.letter): count += 1
        except IndexError:
            continue
    print(count)

lines = load('2020/data/day_02')
content = parse(lines)
password_range_policy_validator(content)
password_position_policy_validator(content)
