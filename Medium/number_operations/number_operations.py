import sys
import operator
import itertools

operators = {'+': operator.add, '-': operator.sub, '*': operator.mul}
ops = ['+', '-', '*']
combos = []
for a in ops:
    for b in ops:
        for c in ops:
            for d in ops:
                combos.append([a, b, c, d])

def calculation(combo, nums, idx, initial_value):
    if idx == 0:
        initial_value += operators[combo[idx]](nums[idx],nums[idx+1])
        idx += 1
        calculation(combo,nums,idx,initial_value)
    elif idx < (len(nums) - 1) and idx > 0:
        initial_value = operators[combo[idx]](initial_value,nums[idx+1])
        idx += 1
        calculation(combo, nums, idx, initial_value)
    else:
        final_value.append(str(initial_value))

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        numbers = map(int,test.rstrip('\n').split())
        permutations = set(itertools.permutations(numbers))
        result = ''
        for c in combos:
            for f in permutations:
                final_value = []
                calculation(c,f,0,0)
                if ''.join(final_value) == '42':
                    result = 'YES'
                    break
                else:
                    result = 'NO'
            if result == 'YES':
                break
        print result