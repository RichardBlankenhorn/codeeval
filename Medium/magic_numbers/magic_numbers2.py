import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        li = map(int, test.split())
        uniques = []
        the_final_li = []
        for val in range(li[0], li[1] + 1):
            if len(list(str(val))) == len(set(list(str(val)))):
                uniques.append(str(val))
        for item in uniques:
            li_num = list(item)
            summed = sum(map(int, li_num))
            times = (summed / len(li_num)) + 1
            new_unique = li_num*times
            indexes = map(int,new_unique)
            final_li = []
            start = indexes[0]
            count = 0
            while count < len(li_num):
                final_li.append(indexes[start])
                start = indexes.index(indexes[start]) + indexes[start]
                count += 1
            if str(final_li[-1]) == li_num[0] and set(map(str,final_li)) == set(li_num):
                final_li = map(str, final_li)
                the_final_li.append(''.join(final_li[::-1]))
        if len(the_final_li) > 0:
            print ' '.join(the_final_li)
        else:
            print "-1"
