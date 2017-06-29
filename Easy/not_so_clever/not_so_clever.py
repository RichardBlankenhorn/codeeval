import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        li = list(test.replace('|', ' ').split())
        num_of_iterations = int(li.pop())
        num_list = map(lambda x : int(x), li)
        length = len(num_list)
        count = 0
        index = 1
        x = True
        i = 0
        while x and i < num_of_iterations:
            if index == length:
                x = False
            elif num_list[count] > num_list[index]:
                tmp_a = num_list[count]
                tmp_b = num_list[count+1]
                num_list[count] = tmp_b
                num_list[count+1] = tmp_a
                count = 0
                index = 1
                i += 1
            else:
                index += 1
                if count < length-2:
                    count += 1

        sorted_list = map(lambda x : str(x), num_list)
        print ' '.join(sorted_list)