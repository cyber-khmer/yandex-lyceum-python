n = int(input())
my_set1, my_list, my_set2 = set(), [], set()
for _ in range(n):
    my_list.append(input())

for cats in my_list:
    if my_list.count(cats) == 2:
        my_set1.add(cats)
    elif my_list.count(cats) >= 3:
        my_set2.add(cats)

if my_set1:
    print(*my_set1, sep='\n')
else:
    print(None)
print()
if my_set2:
    print(*my_set2, sep='\n')
else:
    print(None)