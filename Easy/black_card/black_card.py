import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        names, number = test.rstrip('\n').replace(' | ', '|').split('|')
        names = list(names.split())
        number = int(number)
        count = 0
        x = True
        while x:
            for index, value in enumerate(names):
                if len(names) == 1:
                    x = False
                    break
                elif count+1 == number:
                    names.pop(index)
                    count = 0
                    break
                else:
                    count += 1
        print ''.join(names)