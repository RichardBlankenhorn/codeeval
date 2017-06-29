import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        number = int(test)
        mersenne_numbers = []
        primes = [2,3,5,7,11]
        for i in primes:
            mersenne = (2**i) - 1
            if mersenne < number:
                mersenne_numbers.append(str(mersenne))
        print ', '.join(mersenne_numbers)
