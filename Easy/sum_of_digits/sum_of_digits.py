import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        num_lis = list(test)
        num_lis[-1] = num_lis[-1].rstrip('\n')
        if num_lis[-1] == '':
            del num_lis[-1]
        tot = 0
        for value in num_lis:
            tot += int(value)
        print tot