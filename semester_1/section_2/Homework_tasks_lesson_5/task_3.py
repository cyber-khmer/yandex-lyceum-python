start, stop, step = int(input()), int(input()), int(input())
count_of_zero = [str(oct(i)[2:]).count('0') for i in range(start, stop, step)]
print(max(count_of_zero))
