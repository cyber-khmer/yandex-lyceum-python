s = input().strip('@#$&*')

while 'AB' in s or 'CBB' in s or 'DBBB' in s:
    if 'AB' in s:
        s = s.replace('AB', 'C', 1)
    elif 'CBB' in s:
        s = s.replace('CBB', 'D', 1)
    elif 'DBBB' in s:
        s = s.replace('DBBB', 'A', 1)

print(s)