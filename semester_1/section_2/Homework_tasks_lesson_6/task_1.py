n, m = int(input()), int(input())
my_list = [int(input()) for _ in range(m)]
my_dict = {}
for i in range(1, n + 1):
    my_dict[i] = my_list.count(i)

print(my_dict)
