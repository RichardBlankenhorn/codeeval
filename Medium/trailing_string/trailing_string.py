import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        string, test_string = test.rstrip('\n').split(',')
        string = list(string)
        test_string = list(test_string)
        l = len(test_string)
        target_string = string[-l::]
        if target_string == test_string:
            print '1'
        else:
            print '0'