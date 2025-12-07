numbers = int(input())
s_s = int(input())
total = 0
stepen = 0
summa = 0
while numbers > 0:
    last_digit = numbers % 10
    if last_digit >= s_s:
        summa = 0
        break
    osn_s_s = s_s ** stepen * last_digit
    numbers //= 10
    stepen += 1
    summa += osn_s_s

if summa == 0:
    print('Объект не подлежит телепортации.')
elif summa != 0 and '0' not in str(summa):
    print(summa)
    print("Поздравляем с успешной телепортацией!")
else:
    print(summa)
    print('Возможно, в следующий раз получится лучше.')