n = int(input())
my_dict = {}
for _ in range(n):
    s = input().split(', ')
    num = s[1].split()
    key1, key2, value = float(num[0]), float(num[1]), s[0]
    if (key1, key2) in my_dict:
        my_dict[key1, key2] += ', ' + value
    else:
        my_dict[key1, key2] = value
print(my_dict)