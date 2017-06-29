import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        values = test.rstrip('\n').split()
        number = int(values.pop())
        if number <= len(values):
            print values[-number]