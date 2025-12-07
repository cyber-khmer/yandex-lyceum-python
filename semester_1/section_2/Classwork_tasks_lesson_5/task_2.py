start, stop = int(input()), int(input())
print([i for i in range(start, stop + 1) if '0' in str(i)])
print([i for i in range(start, stop + 1) if '0' not in str(i)])