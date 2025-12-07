s1 = input()
s2 = input()
numbers = [(i + ',', j) for i in s1 for j in s2]
for i in numbers:
    print(*i)