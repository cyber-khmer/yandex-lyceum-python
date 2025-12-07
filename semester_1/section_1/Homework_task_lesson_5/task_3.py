col_toy = int(input())
counter = 0
total = 0
for i in range(col_toy):
    total += int(input())
    counter += 1

print(round(total / counter, 2))