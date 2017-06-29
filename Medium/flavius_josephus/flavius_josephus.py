import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        if len(test) > 0:
            li = map(int, test.split(","))
            nums = range(0,li[0])
            poppedNums = []
            count = 1
            x = True
            while x:
                for i,v in enumerate(nums):
                    if count % li[1] == 0:
                        poppedNums.append(nums[i])
                    count += 1
                for item in poppedNums:
                    if item in nums:
                        nums.remove(item)
                if len(nums) < 1:
                    x = False
            print ' '.join(map(str, poppedNums))