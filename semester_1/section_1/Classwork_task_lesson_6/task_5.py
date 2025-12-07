max_temp = float('-inf')
max_day = current_day = 1
number_of_days = int(input())
for i in range(number_of_days):
    while True:
        current_measure = input()
        if current_measure == 'New day':
            break
        if max_temp < float(current_measure):
            max_temp = float(current_measure)
            max_day = current_day

    current_day += 1

print(max_temp, max_day)