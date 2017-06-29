import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        string = ''.join(test.rstrip('\n'))
        number = int(string)
        if number % 2 == 0:
            print "1"
        else:
            print "0"