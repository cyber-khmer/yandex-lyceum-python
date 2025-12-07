start, stop = int(input()), int(input())
numbers = []
for i in range(start, stop + 1):
    i_bin = bin(i)[2:]
    if i % 2 == 0:
        i_bin = '11' + i_bin + '0'
    else:
        i_bin += '10'

    numbers.append(int(i_bin, 2))

print(min(numbers), max(numbers))