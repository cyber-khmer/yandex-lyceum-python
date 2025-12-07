n = int(input())
for i in range(1, n + 1):
    if 5 <= i <= 20 or 5 <= i % 10 <= 9 or i == 111 or i % 10 == 0 or 105 <= i <= 120:
        print(f'{i} овец')
    elif 2 <= i <= 4 or 2 <= i % 10 <= 4:
        print(f'{i} овцы')
    elif (i == 1 or i % 10 == 1) and i != 111:
        print(f'{i} овца')