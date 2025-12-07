numbers = []
while (number := int(input())) % 111 != 0:
    numbers.append(number)

for i in range(len(numbers)):
    if numbers[0] < numbers[i] < numbers[-1]:
        print(numbers[i], end=' ')