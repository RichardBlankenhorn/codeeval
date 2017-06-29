import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        string = test.rstrip('\n')
        count = 1
        while count <= len(string):
            subString = string[0:count]
            if string.count(subString) * len(subString) == len(string):
                print str(len(subString))
                break
            count += 1