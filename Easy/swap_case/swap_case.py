import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        letter_list = test.rstrip('\n')
        changed_letters = []
        for char in letter_list:
            if char.isalpha() and char.isupper():
                changed_letters.append(char.lower())
            elif char.isalpha() and char.islower():
                changed_letters.append(char.upper())
            else:
                changed_letters.append(char)
        print ''.join(changed_letters)
