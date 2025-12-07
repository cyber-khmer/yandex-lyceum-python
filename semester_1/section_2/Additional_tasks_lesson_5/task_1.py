s = input().split()
ALPHA = 'aeyuio'
information = []
for string in s:
    information.append(string.lower())
    information.append(len(string))
    counter = sum([1 for i in string.lower() if i in ALPHA])
    total = sum([ord(el) for el in string.lower()])
    information.append(counter)
    information.append(len(set(string)))
    information.append(total)
    print(information)
    information.clear()