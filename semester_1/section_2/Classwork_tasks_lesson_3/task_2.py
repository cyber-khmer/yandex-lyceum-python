n = int(input())
my_set1, my_set2 = set(), set()
for _ in range(n):
    my_set1.add(input())

x = int(input())
for _ in range(x):
    my_set2.add(input())

print(*my_set1.difference(my_set2))