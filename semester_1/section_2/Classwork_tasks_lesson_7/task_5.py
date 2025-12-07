from itertools import product

s1, s2, s3 = input().split(), input().split(), input().split()
for el in product(s1, s2, s3):
    print(', '.join(el))