start, stop, col_numb_in_str = int(input()), int(input()), int(input())
counter = 1
item = 0
if start % 2 == 1:
    start += 1
while True:
    if start > stop:
        break
    if start % 2 == 0:
        if counter % 2 == 0:
            print()
            for j in range(col_numb_in_str * 2 - 1, -1, -1):
                if j % 2 == 0:
                    if item == col_numb_in_str:
                        break

                    if start + j <= stop:
                        print(start + j, end='  ')
                    else:
                        print('', end='    ')
                    item += 1

            counter += 1
            item = 0

        else:
            if counter != 1:
                print()
            for j in range(col_numb_in_str * 2):
                if j % 2 == 0:
                    if item == col_numb_in_str:
                        break

                    if start + j > stop:
                        break
                    print(start + j, end='  ')
                    item += 1

            counter += 1
            item = 0

    start += col_numb_in_str * 2