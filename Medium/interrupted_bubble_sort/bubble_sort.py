import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        nums, iterations = test.rstrip('\n').split('|')
        nums = map(int, nums.split())
        iterations = int(iterations)
        change = len(nums)
        count = 0
        while count < iterations:
            x = 0
            for i,v in enumerate(nums):
                if i < (len(nums) - 1) and v > nums[i+1]:
                    temp = v
                    nums[i] = nums[i+1]
                    nums[i+1] = temp
                    change = i
                    x += 1
            if change == len(nums) or x == 0:
                break
            count += 1
        print ' '.join(map(str, nums))