start = int(input())
stop = int(input())
step = int(input())
if start < stop:
    for i in range(start, stop + 1, step):
        print(i)
else:
    for i in range(start, stop - 1, -step):
        print(i)