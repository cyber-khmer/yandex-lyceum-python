symbol = input()
n = input()
height = (int(c) for c in n)
for h in height:
    print(*[symbol for _ in range(h)], end='\n')
    print(end='\t')