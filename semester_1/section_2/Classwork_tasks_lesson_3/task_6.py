n = int(input())
my_set1 = set(input())
my_set2 = set(input())
my_set3 = my_set2.intersection(my_set1)
for _ in range(n - 2):
    my_set3 = my_set3.intersection(input())


print(*my_set3)