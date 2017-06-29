import sys

def compare_lists(list1,list2):
    start = 0
    end = 2
    count = 0
    z = True
    while z:
        first = list1[start:end]
        second = list2[start:end]
        if set(first+second) == set(code):
            count += 1
        start += 1
        end += 1
        if end > len(list1):
            z = False
    return count

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        sections = map(list, test.rstrip('\n').replace(' ','').split('|'))
        code = ['c','o','d','e']
        l = len(sections)
        total = 0
        for i,v in enumerate(sections):
            if i == l-1:
                break
            else:
                total += compare_lists(v,sections[i+1])
        print str(total)