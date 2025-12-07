s = input().split()
my_dict = {i: ''.join(set(i.lower())) for i in s}
print(my_dict)