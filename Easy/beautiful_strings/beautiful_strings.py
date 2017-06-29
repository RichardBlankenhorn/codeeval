import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        string = test.rstrip('\n').upper()
        unique = set(string)
        start = 26
        counts = []
        for value in unique:
            if value.isalpha() == True:
                counts.append(string.count(value))
        sorted_nums = sorted(counts, reverse=True)
        final_tally = []
        for item in sorted_nums:
            final_tally.append(item*start)
            start -= 1
        print sum(final_tally)