energy = input()
len_energy = len(energy)
while (s := input()) != 'Можно спать.':
    if len(s) % 3 == 0:
        len_energy -= len(s) // 3
    elif len(s) % 2 == 0 and len(s) % 3 != 0:
        len_energy -= len(s) // 2
    else:
        len_energy -= 1
    if len_energy <= 0:
        len_energy = s
        break

print(len_energy)
