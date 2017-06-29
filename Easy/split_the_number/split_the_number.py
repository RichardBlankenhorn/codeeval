import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        nums, pattern = test.rstrip('\n').split()
        nums = list(nums)
        for index, i in enumerate(list(pattern)):
            if i == '+' or i == '-':
                a = int(''.join(nums[index:]))
                b = int(''.join(nums[0:index]))
                if i == '-':
                    print str(b-a)
                else:
                    print str(a+b)