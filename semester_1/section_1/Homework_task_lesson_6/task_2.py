n = int(input())
green_count = 0
blue_count = 0
for i in range(n):
    s = input()
    if 'green' in s and 'red' not in s:
        green_count += 1
    if 'blue' in s and 'red' not in s:
        blue_count += 1

if blue_count == 0:
    print(-1)
else:
    average = green_count / blue_count * 100
    print(round(average))
