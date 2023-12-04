with open('1.txt', encoding='utf-8') as f:
    line_count1 = 0
    list_1 = []
    dict_1 = {}
    for line in f:
        list_1.append(line.strip())
        line_count1 += 1
    value = ['1.txt'] + [str(line_count1)] + list_1
    dict_1[line_count1] = value
    print(dict_1)
    
with open('2.txt', encoding='utf-8') as f:
    line_count2 = 0
    list_2 = []
    dict_2 = {}
    for line in f:
        list_2.append(line.strip())
        line_count2 += 1
    value = ['2.txt'] + [str(line_count2)] + list_2
    dict_2[line_count2] = value
    print(dict_2)
        
with open('3.txt', encoding='utf-8') as f:
    line_count3 = 0
    list_3 = []
    dict_3 = {}
    for line in f:
        list_3.append(line.strip())
        line_count3 += 1
    value = ['3.txt'] + [str(line_count3)] + list_3
    dict_3[line_count3] = value
    print(dict_3)

sum_dict = dict_1 | dict_2 | dict_3
print(sum_dict)
sort_dict = dict(sorted(sum_dict.items()))
print(sort_dict)

with open ('4.txt', 'w', encoding='utf-8') as f:
    for line in sort_dict[1]:
        f.write(line + '\n')
    for line in sort_dict[8]:
        f.write(line + '\n')
    for line in sort_dict[9]:
        f.write(line + '\n')