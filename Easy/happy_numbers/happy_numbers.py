import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        num_lis = list(test)
        num_lis[-1] = num_lis[-1].rstrip('\n')
        if num_lis[-1] == '':
            del num_lis[-1]
        tot = 0
        count = 0
        while count <= 100:
            for num in num_lis:
                num = int(num)
                tot += (num*num)
            if tot == 1:
                print "1"
                break
            elif count == 100:
                print "0"
            else:
                num_lis = list(str(tot))
                tot = 0
            count += 1