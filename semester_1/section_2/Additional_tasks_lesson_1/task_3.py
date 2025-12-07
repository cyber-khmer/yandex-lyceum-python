s = input()

counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
for el in s:
    if el.isalpha() and el.isupper():
        counter1 += 1
    elif el.isalpha() and el.islower():
        counter2 += 1
    elif el.isdigit():
        counter3 += 1
    else:
        counter4 += 1

print('Прописные буквы:', counter1)
print('Строчные буквы:', counter2)
print('Цифры:', counter3)
print('Другие символы:', counter4)