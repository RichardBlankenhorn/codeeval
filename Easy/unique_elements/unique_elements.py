import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        li = test.rstrip('\n').split(',')
        the_list = []
        for item in li:
            the_list.append(int(item))
        final_list = set(the_list)
        new_lis = sorted(final_list)
        ordered_list = map(lambda y : str(y), new_lis)
        print ','.join(ordered_list)

