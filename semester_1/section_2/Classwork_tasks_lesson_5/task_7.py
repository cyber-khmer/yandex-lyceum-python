from math import ceil

animals = input().split(' : ')
item = int(input())
print('; '.join([a for a in animals * ceil(item / len(animals))][:item]))