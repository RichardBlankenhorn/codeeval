count = 999
index = 0
x = True
while x:
    string_num = str(count)
    if string_num == string_num[::-1]:
        string_num = int(string_num)
        for i in list(range(2,count)):
            if string_num % i == 0:
                index += 1
        if index == 0:
            print string_num
            x = False
    count = count - 1
    index = 0

