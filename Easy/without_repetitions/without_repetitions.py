import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        li = test.rstrip('\n').split()
        final_list = []
        for item in li:
            s = ""
            length = len(item)
            for index,char in enumerate(item):
                if (index < length - 1) and (char != item[index+1]):
                    s += char
                elif index == length - 1:
                    s += char
            final_list.append(s)
        print ' '.join(final_list)