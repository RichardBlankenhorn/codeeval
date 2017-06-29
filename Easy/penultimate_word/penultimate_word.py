import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        word_list = test.rstrip('\n').split()
        print word_list[-2]