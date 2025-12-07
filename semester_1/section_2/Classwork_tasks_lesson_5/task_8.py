n, m = int(input()), int(input())
massive = [[i * m + j + 1 for j in range(m)] for i in range(n)]
print(*massive, sep='\n')
