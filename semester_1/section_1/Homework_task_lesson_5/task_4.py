language = input()
step = int(input())
word = input()

for symb in word:
    if language == 'РУС':
        lb, len_alpha = ord('А'), 32
    elif language == 'ENG':
        lb, len_alpha = ord('A'), 26
    new_ord = lb + (ord(symb) - step - lb) % len_alpha
    print(chr(new_ord), end='')