import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        hex,binary = test.rstrip('\n').split('|')
        hex = hex.split()
        binary = binary.split()
        hex_values = [int(h, 16) for h in hex]
        binary_values = [int(b, 2) for b in binary]
        sum_hex = sum(hex_values)
        sum_binary = sum(binary_values)
        if sum_binary == sum_hex or sum_binary > sum_hex:
            print "True"
        else:
            print "False"
