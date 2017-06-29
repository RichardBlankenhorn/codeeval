import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        nums = map(int, test.rstrip('\n').split())[1:]
        options = range(min(nums),max(nums)+1)
        totals = []
        for v in options:
            differences = []
            for val in nums:
                differences.append(abs(v-val))
            totals.append(sum(differences))
        print str(min(totals))