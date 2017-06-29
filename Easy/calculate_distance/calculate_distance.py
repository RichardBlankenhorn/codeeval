import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        point1, point2 = test.rstrip('\n').replace(', ',',').replace(')', '').replace('(','').split()
        set1 = map(int, point1.split(','))
        set2 = map(int, point2.split(','))
        distance_x = (set1[0] - set2[0])**2
        distance_y = (set1[1] - set2[1])**2
        length = str(int((distance_x + distance_y)**.5))
        print length