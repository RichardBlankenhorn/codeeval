import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        lis = test.replace(';', '').replace(',', '').split()
        digs = []
        for c in lis:
            digs.append(int(''.join([char for char in c if char.isdigit()])))
        digs.insert(0,0)
        sort = sorted(digs)
        count = 0
        while count < len(sort) - 1:
            sort[count] = sort[count+1] - sort[count]
            count += 1
        sort.pop()
        print ','.join(map(lambda x : str(x), sort))
