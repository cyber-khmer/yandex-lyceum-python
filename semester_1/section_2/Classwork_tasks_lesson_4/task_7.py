result = []
while (s := input()) != '':
    s = s.split()
    name_surname = ' '.join(s[:2])
    score = int(s[2]) + int(s[3]) + int(s[4])
    result.append((-score, name_surname))

result.sort()
for i in result[:5]:
    print(i[1])

mesto = 5
while result[mesto][0] == result[4][0]:
    mesto += 1

print(mesto - 5)