stop, start = int(input()), int(input())
current_day = 1
item = 0
for i in range(1, stop + start):
    if i >= start:
        if item == 7:
            print()
            item = 0
        print(current_day, end='\t')
        current_day += 1
    else:
        print('', end='\t')
    item += 1