way = {}
while (s := input()) != 'КОНЕЦ МАРШРУТА':
    s = s.split('\t')
    way[int(s[1])] = s[0]

numbers = sorted(way.keys())
print(' - '.join([way[key] for key in numbers]))