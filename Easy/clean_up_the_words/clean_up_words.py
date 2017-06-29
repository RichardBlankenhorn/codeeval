import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        word_list = []
        for item in test:
            if item.isalpha() == True:
                word_list.append(item.lower())
            else:
                word_list.append(" ")
        sentence = ''.join(word_list).lstrip().rstrip()
        while '  ' in sentence:
            sentence = sentence.replace('  ', ' ')
        print sentence