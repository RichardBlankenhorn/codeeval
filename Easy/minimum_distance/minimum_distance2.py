import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        nums = map(int, test.rstrip('\n').split())
        count = nums.pop(0)
        nums = sorted(nums)
        if count % 2 == 0:
            median = (nums[count/2 - 1] + nums[count/2])/2
        else:
            median = nums[count/2]
        totals = [abs(v-median) for v in nums]
        print str(sum(totals))