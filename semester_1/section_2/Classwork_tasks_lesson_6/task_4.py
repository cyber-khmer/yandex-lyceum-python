s = input()
numbers = [int(i) for i in s if i.isdigit()]
numbers.sort()
count_of_numbers = {}
for number in numbers:
    count_of_numbers[number] = count_of_numbers.get(number, 0) + 1

print(count_of_numbers)