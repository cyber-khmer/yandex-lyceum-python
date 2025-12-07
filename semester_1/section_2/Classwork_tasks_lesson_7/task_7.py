from itertools import product, repeat

s = input().split()
k, n, m = int(s[0]), int(s[1]), int(s[2])
string = '012345'
ind = 0
for num in product(string, repeat=k):
    ind += 1
    if ind >= m:
        break
    if ind >= n:
        print(''.join(num))