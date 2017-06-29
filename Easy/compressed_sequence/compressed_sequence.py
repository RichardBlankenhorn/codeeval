import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        nums = test.rstrip('\n').split()
        num_list = []
        x = True
        length = len(nums)
        count = 1
        while x:
            for i,n in enumerate(nums):
                if i+1 == length:
                    num_list.append(str(count))
                    num_list.append(n)
                    x = False
                    break
                elif n == nums[i+1]:
                    count += 1
                else:
                    num_list.append(str(count))
                    num_list.append(n)
                    count = 1
        print ' '.join(num_list)
