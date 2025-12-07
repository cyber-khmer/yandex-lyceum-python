n = int(input())
my_set = set()
for i in range(n):
    while (s := input()) != '':
        my_set.add(s)

print(*sorted(my_set), sep='\n')