s = input()
if s.count('O') > s.count('X'):
    print('II')
elif s.count('X') > s.count('O'):
    print('I')
else:
    if s.count('X') == s.count('O') and s.find('X') < s.find('O'):
        print('I')
    else:
        print('II')