n = input().split('.')
for i in range(len(n)):
    s = bin(int(n[i]))[2:]
    print(s.zfill(8), end='')