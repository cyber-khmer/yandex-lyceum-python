my_list = []
function = {'I': 0, 'II': 0, 'III': 0, 'IV': 0, 'X': 0, 'Y': 0}

while (s := input()) != '':
    points = s.split()
    for el in points:
        el = el.split(',')
        row = [float(el[0]), float(el[1])]
        my_list.append(row)

for i in range(len(my_list)):
    x = my_list[i][0]
    y = my_list[i][1]
    if x > 0 and y > 0:
        function['I'] += 1
    elif x < 0 < y:
        function['II'] += 1
    elif x < 0 and y < 0:
        function['III'] += 1
    elif x > 0 > y:
        function['IV'] += 1
    elif x == 0 and y != 0:
        function['Y'] += 1
    elif y == 0 and x != 0:
        function['X'] += 1
    elif x == 0 and y == 0:
        function['X'] += 1
        function['Y'] += 1

print(function)
