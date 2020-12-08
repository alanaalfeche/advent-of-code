from collections import namedtuple
import re

from data import load_day


def count_passports_with_all_required_fields(fields, passports):
    passports_with_all_required_fields = 0
    valid_passports = 0
    one_passport = []
    for line in passports:
        if not line:
            tmp = ' '.join(one_passport)
            if all(field in tmp for field in fields):
                passports_with_all_required_fields += 1
                valid_passports += validate(tmp)
            one_passport = []
            continue
        one_passport.append(line)

    print(f'Number of passport with all required fields: {passports_with_all_required_fields}')
    print(f'Number of actual valid passports: {valid_passports}')

def validate(passport):
    """Rules:
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
    """
    valid = []
    fields = passport.split(' ')
    for field in fields:
        key, value = field.split(':')
        if key == 'byr':
            if 1920 <= int(value) <= 2002: valid.append(True)
            else: valid.append(False)
        elif key == 'iyr':
            if 2010 <= int(value) <= 2020: valid.append(True)
            else: valid.append(False)
        elif key == 'eyr':
            if 2020 <= int(value) <= 2030: valid.append(True)
            else: valid.append(False)
        elif key == 'hgt':
            num = int(re.findall('\d+', value)[0])
            if 'cm' in value and (150 <= num <= 193): valid.append(True)
            elif 'in' in value and (59 <= num <= 76): valid.append(True)
            else: valid.append(False)
        elif key == 'hcl':
            if len(value) == 7 and re.search('^#[0-9a-f]', value): valid.append(True)
            else: valid.append(False)
        elif key == 'ecl':
            valid_eye_color= ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            if value in valid_eye_color: valid.append(True)
            else: valid.append(False)
        elif key == 'pid':
            if len(value) == 9 and re.search('^0', value): valid.append(True)
            else: valid.append(False)
        elif key == 'cid': valid.append(True)
        
    return all(valid)

passports = load_day(4)
required_passport_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
count_passports_with_all_required_fields(required_passport_fields, passports)
