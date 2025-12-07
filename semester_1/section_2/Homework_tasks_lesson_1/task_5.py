s = input()
step_of_rat = input()[::-1]
step_of_rat = int(step_of_rat)
i = 0
step = 0
while s != '':
    eaten_part = step_of_rat % 10
    print(s[i:i + eaten_part] if step % 2 == 0 else s[i:i + eaten_part][::-1])
    last_eater = "ПЕРВЫЙ" if step % 2 == 0 else "ВТОРОЙ"
    step_of_rat //= 10
    s = s.replace(s[i:i + eaten_part], '')[::-1]
    step += 1

print(last_eater)