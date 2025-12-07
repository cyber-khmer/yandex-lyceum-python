my_list = []
while (s := input()) != '':
    my_list.append((s[:s.find(' ')], int(s[s.find(' '):])))

my_dict = dict(my_list)
print(my_dict)