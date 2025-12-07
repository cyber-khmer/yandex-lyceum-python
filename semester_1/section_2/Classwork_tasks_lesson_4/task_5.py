n = int(input())
matrix = []
for i in range(n):
    s = input().split()
    matrix.append(s)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(int(matrix[i][j]) + i + 1, end=' ')

    print()