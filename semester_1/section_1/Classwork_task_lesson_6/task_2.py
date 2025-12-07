bred = int(input())
timer = int(input())
total = 0
for i in range(timer):
    if total >= bred:
        break
    number = int(input())
    total += number

if total >= bred:
    print(f'Ваша хлеб уже готов! Степень поджаривания {total}.')
else:
    print(f'Хлеб поджарен до степени {total}.')
