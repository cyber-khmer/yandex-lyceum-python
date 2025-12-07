n = int(input())
my_dict = {}
for _ in range(n):
    s = input().split('\t')
    my_dict[s[0]] = s[1]

n = int(input())
for _ in range(n):
    res = my_dict.get(input(), 'Нет данных.')
    print(res)