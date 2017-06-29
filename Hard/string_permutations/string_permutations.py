import sys

def recursion(l,n,x):
    if n < x:
        for indexes[n],vars[n] in enumerate(l):
            recursion(l,n+1,x)
    else:
        if len(set(indexes[0:x])) == len(li):
            t.append(vars[0:x])


with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        li = test.rstrip('\n')
        vars = ["li"+str(count) for count in range(0,len(li))]
        indexes = ["idx"+str(c) for c in range(0,len(li))]
        t = []
        recursion(li,0,len(li))
        print ','.join(sorted(map(''.join, t)))