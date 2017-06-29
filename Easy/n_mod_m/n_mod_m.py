import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        nums = map(int, test.rstrip('\n').split(','))
        if nums[0] < nums[1]:
            print str(nums[0])
        else:
            div = nums[0]/nums[1]
            print str(nums[0] - (div*nums[1]))