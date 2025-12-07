n = int(input())
diploma = {}
for _ in range(n):
    s = input().rsplit(' ', 2)
    diploma[s[0]] = (int(s[1]), int(s[2]))

isBreak = False
marks = input().split()
if int(marks[-1]) < 50 and '0' not in marks:
    print('благодарность')
else:
    total = sum([int(marks[i]) for i in range(len(marks) - 1)])

    for keys, values in diploma.items():
        if values[0] <= total < values[1]:
            print(keys)
            isBreak = True
            break

    if not isBreak:
        print('благодарность')
