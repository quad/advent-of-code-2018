from operator import itemgetter
import string
import re


test_input = "dabAcCaCBAcCcaDA"


def reduce_polymer(polymer):
    list_polymer = list(polymer)
    char_lookup = string.ascii_letters + string.ascii_lowercase
    char_index = {a[1]: a[0] for a in enumerate(string.ascii_letters)}
    i = 0
    while(i < len(list_polymer) - 1):
        if list_polymer[i - 1] == char_lookup[char_index[list_polymer[i]] + 26]:
            list_polymer = list_polymer[:i - 1] + list_polymer[i + 1:]
            i = 0
        i += 1
    return ''.join(list_polymer)


def puzzle2(polymer):
    results = []
    for char in string.ascii_lowercase:
        re_str = '[{}{}]'.format(char, char.upper())
        print(re_str)
        reduced_polymer = re.sub(re_str, '', polymer)
        results.append((char, len(reduce_polymer(reduced_polymer))))
    results.sort(key=itemgetter(1))
    return results[0]


print(len(reduce_polymer(test_input)))
print(puzzle2(test_input))
with open('5.txt') as f:
    print(len(reduce_polymer(f.readline().strip())))

with open('5.txt') as f:
    print(puzzle2(f.readline().strip()))
