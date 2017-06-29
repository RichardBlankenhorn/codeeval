import sys
import itertools

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        li = test.rstrip('\n').split(',')
        combos = [list(x) for x in itertools.combinations(li,4)]
        count = 0
        for i,v in enumerate(combos):
            combos[i] = map(int,v)
        for val in combos:
            if sum(val) == 0:
                count += 1
        print str(count)