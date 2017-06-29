import sys

def list_search(li, start):
    new_list = li[start:]
    length = len(new_list)
    index = 1
    count = 0
    x = True
    while index < length/2:
        if new_list[count:index] == new_list[index:index*2]:
            print ' '.join(new_list[count:index])
            return '1'
            break
        index += 1

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        nums = test.rstrip('\n').split()
        for i,v in enumerate(nums):
            if list_search(nums,i) == '1':
                break