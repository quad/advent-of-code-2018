import sys
import re


def parse_string(tokens):
    start_value = 0
    for token in tokens:
        token = re.sub('[^\d+-]', '', token)
        if token[0] == '+':
            start_value += int(token[1:])
        elif token[0] == '-':
            start_value -= int(token[1:])
        else:
            sys.exit("WORLD IS BURNING")
    return start_value


with open(sys.argv[1], 'r') as f:
    print(parse_string(f.readlines()))
