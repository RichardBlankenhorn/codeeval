import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        words_and_nums = test.rstrip('\n').split(',')
        words = []
        nums = []
        for item in words_and_nums:
            if item.isalpha():
                words.append(item)
            elif item.isdigit():
                nums.append(item)
        final_list = []
        if len(words) > 0:
            final_list.append(','.join(words))
        if len(nums) > 0:
            final_list.append(','.join(nums))

        print '|'.join(final_list)
