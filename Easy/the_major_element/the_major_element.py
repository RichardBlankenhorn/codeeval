import sys
from collections import Counter

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        num_list = test.rstrip('\n').split(',')
        length = len(num_list)
        counts = Counter(num_list)
        max = counts.most_common(1)[0][0]
        times = counts.most_common(1)[0][1]
        if times > (length/2):
            print max
        else:
            print 'None'