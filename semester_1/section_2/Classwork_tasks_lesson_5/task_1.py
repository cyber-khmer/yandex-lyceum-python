start, stop = int(input()), int(input())
print([oct(i)[2:] for i in range(start, stop)])