n = int(input())
my_dict = {}
for _ in range(n):
    key, value = input(), input().split(',')
    my_list = [int(i) for i in value]
    my_dict[key] = my_list

k = input()
print(min(my_dict[k]))