import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        number_list = test.rstrip('\n').replace(',', ' ').split(';')
        nums1, nums2 = map(lambda x: x.split(' '), number_list)
        intersection = []
        for value in nums1:
            if value in nums2:
                intersection.append(value)
        print ','.join(intersection)