import sys

numbers = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6,
           'seven': 7, 'eight': 8, 'nine': 9}

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        number_list = test.rstrip('\n').split(';')
        actual_numbers = []
        for num in number_list:
            if num in numbers.keys():
                actual_numbers.append(str(numbers[num]))
        print ''.join(actual_numbers)
