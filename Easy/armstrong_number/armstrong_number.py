import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        numbers = map(int, list(test.rstrip('\n')))
        length = len(numbers)
        roots = map(lambda x : x**length, numbers)
        new_num = str(sum(roots))
        numbers = ''.join(map(str, numbers))
        if new_num == numbers:
            print "True"
        else:
            print "False"