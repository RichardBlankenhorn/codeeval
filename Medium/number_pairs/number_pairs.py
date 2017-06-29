import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        nums, target = test.rstrip('\n').split(';')
        new_nums = map(int, nums.split(','))
        new_target = int(target)
        pairs = []
        for i, value in enumerate(new_nums):
            for k, item in enumerate(new_nums[i+1::]):
                if value + item == new_target:
                    pairs.append(str(value) + ',' + str(item))
        if len(pairs) == 0:
            print "NULL"
        else:
            print ';'.join(pairs)