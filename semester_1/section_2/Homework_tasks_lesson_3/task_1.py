my_set = set()
while (s := input()) != 'УБЕЖАЛ!':
    my_set.add(s)

print(*my_set, sep=', ')