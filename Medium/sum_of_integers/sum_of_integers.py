import sys

with open(sys.argv[1], 'r') as test_cases:
    num_lis = []
    for test in test_cases:
        test = int(test.rstrip('\n'))
        num_lis.append(test)
    print sum(num_lis)