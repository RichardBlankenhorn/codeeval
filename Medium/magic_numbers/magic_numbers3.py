import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        li = map(int, test.split())
        the_final_li = []
        uniques = [str(val) for val in range(li[0], li[1]+1) if len(list(str(val))) == len(set(list(str(val))))]
        uniques = [value for value in uniques if '0' not in value]
        for item in uniques:
            numbered_list = map(int, list(item))
            times = (sum(numbered_list) / len(numbered_list) + 5)
            new_numbered_list = numbered_list*times
            start = new_numbered_list[0]
            index = new_numbered_list.index(start)
            count = 0
            target_nums = []
            while count < len(numbered_list):
                target_nums.insert(0, new_numbered_list[start])
                start += new_numbered_list[start]
                count += 1
            if set(''.join(map(str,target_nums))) == set(list(item)):
                the_final_li.append(''.join(map(str,target_nums)))
        print the_final_li
