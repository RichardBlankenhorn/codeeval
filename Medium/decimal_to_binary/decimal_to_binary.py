import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        print str(bin(int(test.rstrip('\n')))[2:])