n = int(input())
processes = {}
my_list = [input().split('\t') for _ in range(n)]
for elem in my_list:
    if elem[2] == '0':
        processes[elem[0]] = int(elem[1])
    else:
        temp = [int(processes[i]) for i in elem[2].split(';')]
        maxi_time = max(temp)
        processes[elem[0]] = int(elem[1]) + maxi_time

print(processes)