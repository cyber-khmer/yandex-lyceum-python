from _collections import defaultdict

animals = defaultdict(set)
while (s := input()) != '':
    s = s.split(' - ')
    animals[s[0]].add(int(s[1]))

name_an = input()
print(*sorted(animals[name_an]))