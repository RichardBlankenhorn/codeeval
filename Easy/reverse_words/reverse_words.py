import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        lis = test.split(" ")
        lis[-1] = lis[-1].rstrip('\n')
        if lis[0] != '':
            lis.reverse()
            print ' '.join(lis)