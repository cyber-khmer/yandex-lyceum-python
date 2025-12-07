recipe = {}
number_of_products = {}
lunch = []
while True:
    s = input().split(': ')
    if s[1].endswith('.'):
        recipe[s[0]] = s[1].rstrip('.').split(', ')
        break
    recipe[s[0]] = s[1].rstrip(';').split(', ')

while True:
    s = input().split(': ')
    if s[1].endswith('.'):
        number_of_products[s[0]] = int(s[1].rstrip('.'))
        break
    number_of_products[s[0]] = int(s[1].rstrip(';'))

while (s := input()) != '':
    lunch.append(s)


for food in lunch:
    count_of_product = recipe[food]
    isCooked = True
    for el in count_of_product:
        if el in number_of_products.keys():
            if number_of_products[el] - 1 < 0:
                print(f'Приготовить {food} не получится.')
                isCooked = False
                break
            else:
                number_of_products[el] -= 1
        else:
            print(f'Приготовить {food} не получится.')
            isCooked = False
            break

    if isCooked:
        print(f'Готовим {food}.')