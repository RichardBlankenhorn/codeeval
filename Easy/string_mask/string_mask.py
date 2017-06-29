import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        word, binary = test.rstrip('\n').split()
        wordL = list(word)
        binaryL = list(binary)
        for i,v in enumerate(binaryL):
            if v == '1':
                wordL[i] = wordL[i].upper()
        print ''.join(wordL)
