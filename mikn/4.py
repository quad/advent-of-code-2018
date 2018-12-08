import re
from operator import add, itemgetter
from collections import defaultdict
import datetime


def puzzle1(strings):
    guards = defaultdict(lambda: [0] * 60)
    current_guard = None
    fell_asleep = None
    strings.sort(key=lambda x: x.replace('G', 'a'))
    for string in strings:
        res = re.search(r'^\[[\d\-]+ \d\d:(\d\d)\] (.+?)\s*$', string)
        if not res:
            continue
        min_string, message = res[1], res[2]
        on_duty = re.search(r'^Guard #(\d*) begins shift$', message)
        if on_duty:
            current_guard = int(on_duty[1])
            continue
        if not fell_asleep and re.search(r'falls asleep', message):
            fell_asleep = int(min_string)
            continue
        if re.search(r'wakes up', message):
            mark_minutes = [0] * 60
            for i in range(fell_asleep, int(min_string)):
                mark_minutes[i] += 1
            guards[current_guard] = list(map(add, guards[current_guard], mark_minutes))
            fell_asleep = None


    itemized_guards = list(guards.items())
    itemized_guards.sort(key=lambda x: sum(x[1]), reverse=True) # part 1
    itemized_guards.sort(key=lambda x: max(x[1]), reverse=True)
    highest_minute = 0
    for i, v in enumerate(itemized_guards[0][1]):
        if itemized_guards[0][1][highest_minute] < v:
            highest_minute = i
    print(itemized_guards[0][0], highest_minute)
    print(itemized_guards[0][0] * highest_minute)


with open('4.txt') as f:
    puzzle1(f.readlines())

test_input = '''[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:30] falls asleep
[1518-11-04 00:36] falls asleep
[1518-11-05 00:55] wakes up
[1518-11-01 00:25] wakes up
[1518-11-01 00:55] wakes up
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
'''

puzzle1(test_input.splitlines())
