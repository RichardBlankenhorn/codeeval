import sys

with open(sys.argv[1], 'r') as test_cases:
        for line in test_cases:
                values = map(int, line.strip().split())
                abs_values = sorted(abs(values[x] - values[x-1]) for x in xrange(1, len(values)))
                print abs_values
                if abs_values[:-1] == range(1, len(values)-1):
                        print 'Jolly'
                else:
                        print 'Not jolly'