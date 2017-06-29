import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        li = list(test)
        for char in li:
            if li.count(char) == 1:
                print char
                break