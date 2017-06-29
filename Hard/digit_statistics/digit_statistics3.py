import sys

num_li = [0,1,2,3,4,5,6,7,8,9]

end_digits_dict = {0: [0], 1: [1], 2: [2,4,8,6], 3: [3,9,7,1], 4: [4,6], 5: [5], 6: [6], 7: [7,9,3,1],
                   8: [8,4,2,6], 9: [9,1]}

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        x,n = test.rstrip('\n').split()
        x = list(x)
        n = int(n)
        last_num = x.pop()
        if n < len(end_digits_dict[int(last_num)]):
            times = end_digits_dict[int(last_num)]
        else:
            times = end_digits_dict[int(last_num)] * ((n/len(end_digits_dict[int(last_num)])) + 1)
        if len(times) > n:
            while len(times) > n:
                times.pop()

        final_values = []
        for val in num_li:
            final_values.append(str(val) + ": " + str(times.count(val)))
        print ', '.join(final_values)