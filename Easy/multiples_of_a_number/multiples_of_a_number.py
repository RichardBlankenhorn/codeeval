import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        X,N = test.split(",")
        X = int(X)
        N = int(N)
        if N >= X:
            print N
        else:
            count = 2
            while count + 1 > count:
                if N*count >= X:
                    print N*count
                    break
                else:
                    count += 1