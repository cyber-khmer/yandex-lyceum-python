from itertools import product, repeat

s = input()
print('\n'.join([''.join(c) for c in list(product(s, repeat=len(s)))]))