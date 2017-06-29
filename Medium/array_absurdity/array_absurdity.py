import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        nums = test.replace(';',' ').split()
        needed_nums = nums[1].split(',')
        for value in needed_nums:
            c = needed_nums.count(value)
            if c > 1:
                print value
                break
