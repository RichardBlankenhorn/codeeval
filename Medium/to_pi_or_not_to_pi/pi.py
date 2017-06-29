import sys
from mpmath import mp
import math


with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        mp.dps = 5000
        for v in mp.pi:
            print v