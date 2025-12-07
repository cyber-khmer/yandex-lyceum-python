start, stop, step = int(input()), int(input()), int(input())
temp = 0
if step != 2:
    for i in range(start, stop + 1, -1):
        if start - step == i - 1:
            start -= step
            print()
        else:
            if i - 1 == stop + 1 or i - 1 == start - step + 1:
                print(i - 1, end='')
            else:
                print(i - 1, end='+')

else:
    for i in range(start, stop + 1, -1):
        if start - step == i - 1:
            start -= step
        else:
            print(i - 1)