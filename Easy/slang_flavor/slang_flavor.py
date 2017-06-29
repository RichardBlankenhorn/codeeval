import sys

phrase_dict = {1:', yeah!', 2:', this is crazy, I tell ya.', 3:', can U believe this?', 4:', eh?',
                5:', aw yea.', 6:', yo.', 7:'? No way!', 8:'. Awesome!'}
punct_list = ['.','?','!']
count = 0
phrase_index = 1
with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        sentence = list(test.rstrip('\n'))
        sentence_copy = list(test.rstrip('\n'))
        for i, char in enumerate(sentence):
            if char in punct_list:
                count += 1
                if count % 2 == 0:
                    sentence_copy[i] = phrase_dict[phrase_index]
                    phrase_index += 1
                    if phrase_index > 8:
                        phrase_index = 1
        print ''.join(sentence_copy)
