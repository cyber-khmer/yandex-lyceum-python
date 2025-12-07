numbers = []
start, stop = int(input()), int(input())
divider = int(input())
bad_dig = int(input())
for i in range(start, stop):
    if i % divider == 0 and str(bad_dig) not in str(i):
        numbers.append(i)

print(sorted(numbers, reverse = True))