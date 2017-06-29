import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        zero_lis = list(test.split())
        binary_list = []
        length = len(zero_lis)
        x = 0
        val = 1
        factor = 0
        while x < length - 1:
            if zero_lis[x] == '0':
                factor = '0'
            elif zero_lis[x] == '00':
                factor = '1'
            num_zeros = zero_lis[val].count('0')
            binary_list.append(num_zeros*factor)
            x += 2
            val += 2
        binary_number = int(''.join(binary_list),2)
        print binary_number
