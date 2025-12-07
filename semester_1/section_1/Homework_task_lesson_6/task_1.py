day = int(input())
for i in range(1, day + 1):
    if i % 7 == 0:
        print(i, end='\t')
        print()
    else:
        print(i, end='\t')