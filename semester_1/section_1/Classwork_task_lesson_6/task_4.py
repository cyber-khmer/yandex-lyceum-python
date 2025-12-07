alpha = 'aeyuioAEYUIO'
while (s := input()) != '':
    for i in s:
        if i in alpha:
            continue
        print(i, end='')

    print()