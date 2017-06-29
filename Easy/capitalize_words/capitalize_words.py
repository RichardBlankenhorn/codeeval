import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        word_list = test.rstrip('\n').split()
        for i,word in enumerate(word_list):
            sep_word = list(word)
            sep_word[0] = sep_word[0].upper()
            comb_word = ''.join(sep_word)
            word_list[i] = comb_word
        print ' '.join(word_list)