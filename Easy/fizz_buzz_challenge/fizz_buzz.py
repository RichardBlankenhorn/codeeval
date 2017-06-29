#!/usr/bin/env python

import csv

def fizz_buzz(input_list):
    L = len(input_list)
    count = 0
    output_list = []

    while count < L:

        X = int(input_list[count][0])
        Y = int(input_list[count][1])
        N = list(range(1, int(input_list[count][2]) + 1, 1))

        count += 1
        value_list = []
        for value in N:
            if value % Y == 0 and value % X == 0:
                value_list.append('FB')
            elif value % X == 0:
                value_list.append('F')
            elif value % Y == 0:
                value_list.append('B')
            else:
                value_list.append(value)
        output_list.append(value_list)

    with open("output_file.csv", "wb") as o:
        writer = csv.writer(o)
        writer.writerows(output_list)

input_file = "input.csv"
with open(input_file, 'rb') as f:
    reader = csv.reader(f)
    input_list = list(reader)

fizz_buzz(input_list)

