import re

from collections import defaultdict
from data import load_day


bags = defaultdict(dict)
def parse_data(luggage_rules):
    for rule in luggage_rules:
        outside_bag = re.match(r'(.*) bags contain', rule).groups()[0]
        for count, inside_bag in re.findall(r'(\d+) (\w+ \w+) bags?', rule):
            bags[outside_bag][inside_bag] = int(count)
    return bags

answer = set()
def search(color):
    for bag in bags:
        if color in bags[bag]:
            answer.add(bag)
            search(bag)
    return len(answer)

def count(color):
    total = 1
    for bag in bags[color]:
        multiplier = bags[color][bag]
        total += multiplier * count(bag)
    return total

luggage_rules = load_day(7)
parse_data(luggage_rules)
bag = 'shiny gold'
# part a
print(search(bag))
# part b
print(count(bag)-1)
