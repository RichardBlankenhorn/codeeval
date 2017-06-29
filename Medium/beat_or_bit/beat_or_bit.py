import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        values = test.replace(' ','').split('|')
        binaryLi = []
        for item in values:
            binary = []
            for i,v in enumerate(item):
                if i == 0:
                    binary.append(v)
                else:
                    if v == '1':
                        if binary[i-1] == '0':
                            binary.append('1')
                        elif binary[i-1] == '1':
                            binary.append('0')
                    elif v == '0':
                        binary.append(binary[i-1])
            binaryLi.append(str(int(''.join(binary), 2)))
        print ' | '.join(binaryLi)