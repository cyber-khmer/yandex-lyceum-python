my_set1, my_set2 = set(), set()

while (s := input()) != '':
    my_set1.add(s)

while (s := input()) != '':
    my_set2.add(s)

n = int(input())
print(*sorted(my_set1.difference(my_set2) if n == 1 else my_set2.difference(my_set1)), sep='\n')