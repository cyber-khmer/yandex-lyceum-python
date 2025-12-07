n = int(input())
my_set = set()
for i in range(n):
    s = input()
    total = 0
    for el in s:
        total += ord(el.lower()) - ord('a') + 1

    row = (total, s)
    my_set.add(row)

my_set = sorted(my_set)
for el in my_set:
    print(el[1])
