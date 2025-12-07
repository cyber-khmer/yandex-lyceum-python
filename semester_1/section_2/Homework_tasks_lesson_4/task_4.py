n = int(input())
matrix = []
for i in range(n):
    s = input().split()
    row = []
    for el in s:
        row.append(int(el))

    matrix.append(row)

matrix.reverse()
item = n
for i in range(n):
    print(str(item) + ':', *sorted(matrix[i]))
    item -= 1