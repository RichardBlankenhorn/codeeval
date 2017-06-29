import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        numbers = map(int, list(test.rstrip('\n')))
        self_describing = True
        for i,v in enumerate(numbers):
            if numbers.count(i) == v:
                self_describing = True
            else:
                self_describing = False
                break
        if self_describing:
            print "1"
        else:
            print "0"