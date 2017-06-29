import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        string, letter = test.rstrip('\n').split(',')
        if letter in string:
            for i,s in enumerate(string[::-1]):
                if s == letter:
                    index = i
                    break
            print str((len(string) - 1) - index)
        else:
            print str(-1)