string = input()
ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
symb_before = ''
result = ''
for symb in string:
    if symb in ALPHABET:
        result += symb

string = result
result = ''

for symb in string:
    if symb > symb_before and symb in ALPHABET:
        result += symb

    symb_before = symb

string = result
result = ''
flag = False
for symb in string:
    if symb in 'aeiuyoAEIUYO':
        flag = True
        result += symb * 2
    else:
        result += symb
        if flag:
            result += symb
        flag = False

if len(result) == 33:
    print(result)
else:
    i = 1
    for symb in result:
        print(symb, end='\n' if i % 7 == 0 else '')
        i += 1