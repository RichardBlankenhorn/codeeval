import sys

roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        value = list(test.rstrip('\n'))
        for i,item in enumerate(value):
            if item.isdigit() == True:
                value[i] = int(item)
            else:
                value[i] = roman_dict[item]
        new_values = []
        for k,v in enumerate(value):
            if k % 2 != 0 and k != 1:
                if abs(v) > abs(value[k-2]):
                    value[k-2] = value[k-2]*-1
        for index,num in enumerate(value):
            if index % 2 != 0:
                new_values.append(num*value[index-1])
        print str(sum(new_values))
