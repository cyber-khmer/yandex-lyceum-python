n = int(input())
my_set1 = set()
for _ in range(n):
    my_set1.add(input())

x = int(input())
my_set2 = set()
for _ in range(x):
    my_set2.add(input())

print(*my_set1.intersection(my_set2), sep='\n')