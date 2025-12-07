numbers = input().split()
result = []
for i in numbers:
    tmp = bin(int(i))[2:]
    if tmp.count('1') % 2 != 0:
        tmp = '10' + tmp
    else:
        tmp += '10'
    result.append(int(tmp, 2))

print(result)