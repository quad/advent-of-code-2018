import sys
import re


def parse_string(tokens, i_love_sets, curr_value=0):
    print(tokens)
    for token in tokens:
        token = re.sub('[^\d+-]', '', token)
        if token[0] == '+':
            curr_value += int(token[1:])
        elif token[0] == '-':
            curr_value -= int(token[1:])
        else:
            sys.exit("WORLD IS BURNING")
        if curr_value in i_love_sets:
            return curr_value, True
        i_love_sets.add(curr_value)
    return curr_value, False


with open(sys.argv[1], 'r') as f:
    tokens = f.readlines()
    i_love_this_set = set([0])
    curr_value, first_double = parse_string(tokens, i_love_this_set)
    while not first_double:
        curr_value, first_double = parse_string(tokens, i_love_this_set, curr_value)
    print(curr_value)
