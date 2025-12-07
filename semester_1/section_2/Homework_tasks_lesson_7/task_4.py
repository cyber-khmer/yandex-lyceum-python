from collections import Counter

n = int(input())
things = []

for i in range(n):
    things.extend(input().split(': ')[1].split(', '))

counter = Counter(things)
res = list(counter.items())
for i in range(0, len(res)):
    current_max = res[i]
    max_ind = i

    for j in range(i, len(res)):
        if res[j][1] > current_max[1] or \
                res[j][1] == current_max[1] and res[j][0] > current_max[0]:
            current_max = res[j]
            max_ind = j

    res[i], res[max_ind] = res[max_ind], res[i]

print('\n'.join([f'{pair[0]} -> {pair[1]}' for pair in res]))