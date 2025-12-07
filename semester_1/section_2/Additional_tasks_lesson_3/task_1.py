my_automat = set()
while (s := input()) != '':
    while '111' in s or '00' in s:
        s = s.replace('111', '0', 1)
        s = s.replace('000', '1', 1)
        s = s.replace('001', '1', 1)
        s = s.replace('100', '1', 1)
        s = s.replace('00', '0', 1)

    my_automat.add(s)

print(len(my_automat))
print(*my_automat, sep='\n')