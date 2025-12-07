from itertools import combinations

s = input().split('\t')
k = int(input())
for el in combinations(s, k):
    print(', '.join(el))