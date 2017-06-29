import sys

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u',
            'v','w','x','y','z']

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        sentence = test.rstrip('\n')
        sentence = list(sentence.lower())
        count = 0
        missing_letters = []
        for i in alphabet:
            if sentence.count(i) > 0:
                count += 1
            else:
                missing_letters.append(i)
        if count == len(alphabet):
            print 'NULL'
        else:
            print ''.join(missing_letters)
        sums = []
        li = [1,3,6,10,15,21,28,36,45,55,66,78,91,105,105,91,78,66,55,45,36,28,21,15,10,6,3,1]
        for v in li:
            sums.append(v**2)
        print len(sums)
