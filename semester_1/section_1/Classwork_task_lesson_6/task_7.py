while (string := input()) != '':
    if 'BUG' in string or 'bug' in string:
        print(string)
        break

    if 'b' in string and 'u' in string and 'g' in string:
        print('BUG')
    else:
        print()