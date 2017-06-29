import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        values = test.rstrip('\n').split()
        nums = []
        operator = []
        for item in values:
            if item.isalnum() == True:
                nums.append(item)
            else:
                operator.append(item)
        operator.reverse()
        final_expression = []
        for i, (x,y) in enumerate(zip(nums, operator)):
            if i < len(nums) - 1 and len(final_expression) == 0:
                if y == '+':
                    final_expression.append(float(x) + float(nums[i+1]))
                elif y == '*':
                    final_expression.append(float(x) * float(nums[i+1]))
                elif y == '/':
                    final_expression.append(float(x) / float(nums[i+1]))
            elif i < len(nums) - 1:
                if y == '+':
                    final_expression.append(float(final_expression[-1]) + float(nums[i+1]))
                elif y == '*':
                    final_expression.append(float(final_expression[-1]) * float(nums[i+1]))
                elif y == '/':
                    final_expression.append(float(final_expression[-1]) / float(nums[i+1]))
        print str(int(final_expression.pop()))