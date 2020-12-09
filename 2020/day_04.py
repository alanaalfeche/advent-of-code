from collections import namedtuple
import re

from data import load_day


def get_passports_with_all_required_fields(fields, passports):
    passports_with_all_required_fields = []
    one_passport = []
    for line in passports:
        if not line:
            tmp = ' '.join(one_passport)
            if all(field in tmp for field in fields.keys()):
                passports_with_all_required_fields.append(tmp)
            one_passport = []
            continue
        one_passport.append(line)

    return passports_with_all_required_fields

def count_valid_passports(fields, passports):
    no_of_valid_passport = 0
    for passport in passports:
        fields = passport.split(' ')
        parsed_fields = dict(field.split(':') for field in fields)
        no_of_valid_passport += all(v(parsed_fields[k]) for k, v in required_passport_fields.items())
    return no_of_valid_passport
    
passports = load_day(4)
required_passport_fields = {'byr': lambda x: 1920 <= int(x) <= 2002, 
                            'iyr': lambda x: 2010 <= int(x) <= 2020, 
                            'eyr': lambda x: 2020 <= int(x) <= 2030, 
                            'hgt': lambda x: (x.endswith('cm') and 150 <= int(x[:-2]) <= 193) or 
                                             (x.endswith('in') and 59 <= int(x[:-2]) <= 76), 
                            'hcl': lambda x: re.match('^#[0-9a-f]{6}$', x), 
                            'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'], 
                            'pid': lambda x: re.match('^[0-9]{9}$', x)
                            }
good_batch_of_passports = get_passports_with_all_required_fields(required_passport_fields, passports)
valid_passports = count_valid_passports(required_passport_fields, good_batch_of_passports)
print(f'Number of passport with all required fieds: {len(good_batch_of_passports)}')
print(f'Number of valid passports: {valid_passports}')