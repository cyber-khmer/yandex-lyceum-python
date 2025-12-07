n = int(input())
my_set, numbers = set(), []
for _ in range(n):
    numbers.extend(input())

my_set.update(numbers)
print(*my_set, sep=', ')