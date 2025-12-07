n = int(input())

current_tup, current_tup_info = tuple(), tuple()
for i in range(n):
    s = input()
    current_tup, current_tup_info = tuple(), tuple()
    for el in s:
        current_tup += (el,)

    current_tup_info += (len(current_tup), s.count(' '), s.find(' '))
    print(current_tup)
    print(current_tup_info)