n = int(input())

for i in range(n):
    s = input()
    if i % 2 == 0:
        for el in s:
            if el.isalpha() or el.isspace():
                print(el, end='')
        print()

    else:
        for el in s:
            if el.isalpha() or el.isspace() or el.isdigit():
                print(el, end='')
        print()