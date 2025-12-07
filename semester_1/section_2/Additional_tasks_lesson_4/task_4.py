n = int(input())
garage = []
for i in range(n):
    s = input().split()
    row = []
    for j in range(len(s)):
        row.append(int(s[j]))
    garage.append(row)

k = int(input())
for i in range(k):
    position = int(input())
    Notfound = False

    for j in range(len(garage)):
        if position < 0:
            if abs(position) in garage[j]:
                print(f'Освободилось место {j + 1}, {garage[j].index(abs(position)) + 1}')
                garage[j][garage[j].index(abs(position))] = 0
                Notfound = True
                break
        else:
            if 0 in garage[j]:
                print(f'{j + 1}, {garage[j].index(0) + 1}')
                garage[j][garage[j].index(0)] = position
                Notfound = True
                break

    if not Notfound and position > 0:
        print('Мест нет')
