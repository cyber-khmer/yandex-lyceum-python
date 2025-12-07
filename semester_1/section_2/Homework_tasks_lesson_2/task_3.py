item = int(input())
numbers = []
for _ in range(item):
    numbers.append(int(input()))

n = int(input())
maxi = float('-inf')
for i in range(len(numbers)):
    if sum(numbers[i:i + n]) > maxi and len(numbers[i:i + n]) == n:
        maxi = sum(numbers[i:i + n])

print(maxi)