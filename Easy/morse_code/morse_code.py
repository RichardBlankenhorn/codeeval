import sys

morse = {".-" : "A",
        "-..." : "B",
        "-.-." : "C",
        "-.." : "D",
        "." : "E",
        "..-." : "F",
        "--." : "G",
        "...." : "H",
        ".." : "I",
        ".---" : "J",
        "-.-" : "K",
        ".-.." : "L",
        "--" : "M",
        "-." : "N",
        "---" : "O",
        ".--." : "P",
        "--.-" : "Q",
        ".-." : "R",
        "..." : "S",
        "-" : "T",
        "..-" : "U",
        "...-" : "V",
        ".--" : "W",
        "-..-" : "X",
        "-.--" : "Y",
        "--.." : "Z",
        "/" : " ",
         ".----": "1",
         "..---": "2",
         "...--": "3",
         "....-": "4",
         ".....": "5",
         "-....": "6",
         "--...": "7",
         "---..": "8",
         "----.": "9",
         "-----": "0"
        }

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        code = list(test.rstrip('\n').replace('  ', ' / ').split())
        code_list = []
        for c in code:
            if c in morse.keys():
                code_list.append(morse[c])
        print ''.join(code_list)
