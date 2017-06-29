import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        value = int(test.rstrip('\n'))
        l = len(list(str(value)))
        atLeast = int(str(value) + '0')
        for v in xrange(value+1,atLeast + 1):
            if '0' in list(str(v)):
                noZero = filter(lambda x: x != '0', list(str(v)))
                zero = filter(lambda y: y != '0', list(str(value)))
                if sorted(noZero) == sorted(zero):
                    print str(v)
                    break
            else:
                if sorted(list(str(v))) == sorted(list(str(value))):
                    print str(v)
                    break