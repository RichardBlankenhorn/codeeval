import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        li = test.rstrip('\n').split(',')
        li = map(int,li)
        count = 0
        for value in range(li[0], li[1] + 1):
            test_list = []
            for k in range(2,value):
                if value % k == 0:
                    test_list.append(1)
            if sum(test_list) == 0:
                count += 1
        print str(count)