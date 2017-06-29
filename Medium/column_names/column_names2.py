import sys

letter_dict = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I',
               10: 'J', 11: 'K', 12: "L", 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q',
               18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y',
               26: 'Z'}

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        x = int(test)
        letters = []
        y = True
        while y:
            if x <= 26:
                letters.insert(0,letter_dict[x])
                y = False
            elif x > 26:
                if x % 26 == 0:
                    letters.insert(0,letter_dict[26])
                    x = (x/26) - 1
                elif x % 26 != 0:
                    num = (x/26)*26
                    diff = x - num
                    letters.insert(0,letter_dict[diff])
                    x = x/26
        print ''.join(letters)