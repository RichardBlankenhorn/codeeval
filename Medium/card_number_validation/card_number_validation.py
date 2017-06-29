import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        if len(test) > 0:
            nums = list(test.rstrip('\n').replace(' ', ''))
            reversed = nums[::-1]
            for i,v in enumerate(reversed):
                if i != 0 and i % 2 != 0:
                    times = str(int(v)*2)
                    if len(times) > 1:
                        reversed[i] = str(int(times[0]) + int(times[1]))
                    else:
                        reversed[i] = times
            sums = sum(map(int, reversed))
            if sums % 10 == 0:
                print "1"
            else:
                print "0"