import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        values = test.rstrip('\n').split()
        if values != []:
            nums = []
            operator = []
            for item in values:
                if item.isalnum() == True:
                    nums.append(item)
                else:
                    operator.append(item)

            while len(nums) > 1:
                if len(nums) > 1:
                    evaluation = int(eval(nums[0] + operator[-1] + nums[1]))
                    operator.pop()
                    nums[0] = str(evaluation)
                    nums.pop(1)
            print nums[0]