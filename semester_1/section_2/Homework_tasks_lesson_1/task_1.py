s = input()
step = int(input())
number = int(input())
for i in range(0, len(s), step):
    print('Буква под номером', number, '— это', s[i] + '.')
    number += 1