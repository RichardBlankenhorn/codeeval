import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        lis = []
        x,y,z = test.split(" ")
        X = int(x)
        Y = int(y)
        N = int(z.rstrip('\n'))
        numbers = range(1,N+1)

        for value in numbers:
            if value % Y == 0 and value % X == 0:
                lis.append('FB')
            elif value % X == 0:
                lis.append('F')
            elif value % Y == 0:
                lis.append('B')
            else:
                lis.append(str(value))

        print ' '.join(lis)