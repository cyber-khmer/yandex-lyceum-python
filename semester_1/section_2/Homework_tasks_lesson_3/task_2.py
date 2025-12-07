my_set1, my_set2 = set(), set()

while (s := input()) != '':
    my_set1.add(s)

while (s := input()) != '':
    my_set2.add(s)

print(my_set1.difference(my_set2))