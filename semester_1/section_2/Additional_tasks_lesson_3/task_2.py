my_set, my_list = set(), []
n = int(input())
k = 2
while n != 1:
    if n % k == 0:
        my_set.add(k)
        my_list.append(k)
        n //= k
    else:
        k += 1

print(*sorted(my_list))
print(*sorted(my_set))