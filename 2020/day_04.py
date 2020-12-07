from data import load_day

lines = load_day(4)

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
passport = []
valid_passport = 0
for line in lines:
    if not line:
        tmp = ' '.join(passport)
        if all(field in tmp for field in required_fields):
            valid_passport += 1
        passport = []
        continue
    passport.append(line)
print(valid_passport)
