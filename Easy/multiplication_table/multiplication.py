final_list = []
for i in range(1,13):
    lis = []
    for y in range(1,13):
        lis.append(i*y)
    final_list.append(lis)

print('\n'.join([''.join(['{:>4}'.format(num) for num in list]) for list in final_list]))