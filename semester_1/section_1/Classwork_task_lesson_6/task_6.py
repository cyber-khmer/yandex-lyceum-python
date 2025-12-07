total = 0
while (numbers := int(input())) != 17:
    total = 0
    while numbers > 0:
        if (numbers % 10) % 2 != 0:
            total += numbers % 10

        numbers //= 10

    if total == 0:
        break
    print(total)

if total == 0:
    print('Ну, я так не играю!')
else:
    print('Какие замечательные числа!')