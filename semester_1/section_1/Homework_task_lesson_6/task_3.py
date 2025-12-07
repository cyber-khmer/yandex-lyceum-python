from math import dist

event_horizon = float(input())
x, y = int(input()), int(input())
total_distance = 0
while True:
    new_x, new_y = int(input()), int(input())

    if new_x + new_y > 10_000:
        print(round(total_distance, 4))
        break

    distance = dist((x, y), (new_x, new_y))
    print(round(distance, 4))
    total_distance += distance

    if dist((new_x, new_y), (0, 0)) <= event_horizon:
        print('WARNING')
        break



    x, y = new_x, new_y