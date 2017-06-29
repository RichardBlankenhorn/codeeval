import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        li = test.split()
        divider = li.index(":")
        count = 0
        numbers = []
        swaps = []
        while count < len(li):
            if count < divider:
                numbers.append(li[count])
            elif count > divider:
                swaps.append(li[count])
            count += 1
        for i in swaps:
            A,B = (''.join(i).replace('-', " ").replace(',', '')).split(" ")
            A = int(A)
            B = int(B)
            first_num = numbers[A]
            second_num = numbers[B]
            numbers[A] = second_num
            numbers[B] = first_num
        print ' '.join(numbers)


