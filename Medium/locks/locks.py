import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        nums = map(int, test.rstrip('\n').split())
        locks = ['u' for k in range(1,nums[0]+1)]
        count = 0
        while count < nums[1] - 1:
            for i,v in enumerate(locks):
                if (i+1) % 2 == 0:
                    locks[i] = 'l'
            for i,v in enumerate(locks):
                if (i+1) % 3 == 0 and i != 0:
                    if v == 'u':
                        locks[i] = 'l'
                    elif v == 'l':
                        locks[i] = 'u'
            count += 1
        if locks[-1] == 'l':
            locks[-1] = 'u'
        else:
            locks[-1] = 'l'
        print str(locks.count('u'))