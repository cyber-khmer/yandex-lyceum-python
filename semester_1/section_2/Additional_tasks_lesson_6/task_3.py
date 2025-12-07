n = int(input())
res = []
for _ in range(n):
    notation = {}
    number = input().split()
    system_all = [i for i in input().split()]
    notation[number[1]] = number[0]
    for system in system_all:
        s_res = ''
        ten_system = int(number[0], int(number[1]))
        while ten_system > 0:
            if system == '10':
                s_res = str(ten_system)[::-1]
                break
            else:
                s_res += str(ten_system % int(system))
                ten_system //= int(system)

        notation[system] = s_res[::-1]

    res.append(notation)
print(res)
