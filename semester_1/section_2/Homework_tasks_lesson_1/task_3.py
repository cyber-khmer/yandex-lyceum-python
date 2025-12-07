while (s := input()) != '':
    a = s.strip('@#$').rstrip('!,.')
    if a.startswith('And'):
        a = a.replace('and', 'or')
        print(a)
    elif a.endswith('end'):
        a = a.replace('or', 'and')
        print(a)
    else:
        print(a)