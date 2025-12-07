num = input().split()
numbers = [i if int(i) % 3 != 0 else int(i) // 3 for i in num]
print(*numbers, sep=' - ')