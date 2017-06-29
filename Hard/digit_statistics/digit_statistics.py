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
        final_values = []
        if n > len(end_digits_dict[int(last_num)]):
            times = n/len(end_digits_dict[int(last_num)])
            additional = range(n % len(end_digits_dict[int(last_num)]))
            additional = [end_digits_dict[int(last_num)][k] for k in additional]
            for v in num_li:
                if v in end_digits_dict[int(last_num)]:
                    if v in additional:
                        final_values.append(str(v) + ": " + str(times+1))
                    else:
                        final_values.append(str(v) + ": " + str(times))
                else:
                    final_values.append(str(v) + ": " + "0")
        else:
            for v in num_li:
                if v in end_digits_dict[int(last_num)][0:n]:
                    final_values.append(str(v) + ": " + "1")
                else:
                    final_values.append(str(v) + ": " + "0")
        print ', '.join(final_values)

