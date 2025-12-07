import math

words = input().split()
max_len = 0
for word in words:
    if len(word) > max_len:
        max_len = len(word)

for word in words:
    left = '_' * ((max_len - len(word)) // 2)
    right = '_' * (math.ceil((max_len - len(word)) // 2))
    print(left + word + right)