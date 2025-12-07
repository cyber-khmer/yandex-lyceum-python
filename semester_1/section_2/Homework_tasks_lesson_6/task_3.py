n = int(input())
weather = {}
months = {
    '01': 'January',
    '02': 'February',
    '03': 'March',
    '04': 'April',
    '05': 'May',
    '06': 'June',
    '07': 'July',
    '08': 'August',
    '09': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December',
}
for _ in range(n):
    s = input().split()
    number = months[s[0][3:5]]
    weather[number] = weather.get(number, 0) + int(s[1])

print(weather)