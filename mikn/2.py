import collections


def count_letters(test_subject, reps):
    count = collections.defaultdict(int)
    for char in test_subject:
        count[char] += 1
    for c, cnt in count.items():
        if cnt == reps:
            return 1
    return 0


def puzzle1(strings):
    rep2 = 0
    rep3 = 0
    for string in strings:
        rep2 += count_letters(string, 2)
        rep3 += count_letters(string, 3)
    print(f"checksum: {rep2*rep3}")


def puzzle2(strings):
    for string in strings:
        for str_comp in strings:
            diff = 0
            last_diff = 0
            for i in range(len(string)):
                if string[i] != str_comp[i]:
                    diff += 1
                    last_diff = i
                if diff > 1:
                    continue
            if diff == 1:
                print(i)
                print(string[:last_diff] + string[last_diff + 1:])
                print(f"{string}{str_comp}")


with open('2.txt') as f:
    #puzzle1(f.readlines())
    puzzle2(f.readlines())
