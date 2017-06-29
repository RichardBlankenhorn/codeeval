import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        li = map(int, test.split())
        uniques = []
        for val in range(li[0],li[1] + 1):
            if len(list(str(val))) == len(set(list(str(val)))):
                uniques.append(str(val))
        magic = []
        for k in uniques:
            k = map(int, list(k))
            if sum(k) % len(k) == 0:
                magic.append(k)
        print magic
