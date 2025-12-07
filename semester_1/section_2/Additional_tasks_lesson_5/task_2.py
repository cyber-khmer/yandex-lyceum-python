n, m = int(input()), int(input())
inf = [str(j) if j != n else 'КАП' for i in range(m // n) for j in range(1, n + 1)] + \
      [str(j) if j != n else 'КАП' for j in range(1, m % n + 1)]
print(*inf, sep='\n')