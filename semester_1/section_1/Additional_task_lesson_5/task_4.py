start, stop = int(input()), int(input())
for i in range(min(start, stop), max(start, stop)):
    if i % 2 == 0 and i % 8 == 0 and i % 16 == 0:
        print(bin(i), '\t', oct(i), '\t', hex(i), sep='')
    elif i % 2 == 0 and i % 8 == 0:
        print(bin(i), '\t', oct(i), sep='')
    elif i % 2 == 0:
        print(bin(i))
