n = int(input())
my_set1, my_list = set(), []
for _ in range(n):
    s = input()
    my_set1 = my_set1.union(s)
    my_list.append(s)

difference = set()
print(*my_set1, sep='')
for i in range(len(my_list)):
    diff = set(my_list[i])
    for j in range(len(my_list)):
        if i != j:
            diff = diff.difference(set(my_list[j]))

    difference.update(diff)

print(*difference, sep='')