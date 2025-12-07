n = int(input())
numbers = []
for i in range(n):
    x = float(input())
    y = float(input())
    row = [round((x ** 2 + y ** 2) ** 0.5, 3)]
    numbers.append(*row)

print(numbers)