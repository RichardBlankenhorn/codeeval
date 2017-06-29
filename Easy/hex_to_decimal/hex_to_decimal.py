import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        num = int(test, 16)
        print str(num)