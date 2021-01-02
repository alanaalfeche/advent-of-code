import re

from data import load_day


data = load_day(16)
partition = [i for i, ele in enumerate(data) if len(ele) == 0] # entities is separated by empty string

rules = data[:partition[0]]
my_ticket = data[partition[0]+2:partition[1]]
nearby_tickets = data[partition[1]+2:]
# print(rules, my_ticket, nearby_tickets)

invalid = []
for ticket in nearby_tickets:
    tickets = [int(t) for t in ticket.split(',')]

    for ticket in tickets:
        result = []
        for rule in rules:
            rule = re.match(r'(.*): (.*)', rule).groups()[1].split()
            rule_1 = rule[0].split('-')
            rule_2 = rule[2].split('-')

            if int(rule_1[0]) <= ticket <= int(rule_1[1]) or \
                int(rule_2[0]) <= ticket <= int(rule_2[1]):
                result.append(True)
            else:
                result.append(False)

        if not any(result):
            invalid.append(ticket)

        result.clear()

print(sum(invalid))