import sys
from collections import Counter

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        li = test.split()
        the_unique = []
        counts = dict(Counter(li))
        for k,v in counts.items():
            v = int(v)
            if v < 2:
                the_unique.append(int(k))
        if len(the_unique) > 0:
            min_num = min(the_unique)
            print str(li.index(str(min_num)) + 1)
        else:
            print "0"