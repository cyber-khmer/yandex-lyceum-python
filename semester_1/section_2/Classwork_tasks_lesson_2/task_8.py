n = int(input())
monday = []
tuesday = []
wednesday = []
thursday = []
friday = []
saturday = []
sunday = []
for i in range(n):
    day = input()
    match day[:3]:
        case "Mon":
            monday.append(day[4:])
        case "Tue":
            tuesday.append(day[4:])
        case "Wed":
            wednesday.append(day[4:])
        case "Thu":
            thursday.append(day[4:])
        case "Fri":
            friday.append(day[4:])
        case "Sat":
            saturday.append(day[4:])
        case "Sun":
            sunday.append(day[4:])

print(*sorted(monday) if monday else ' ', sep=', ')
print(*sorted(tuesday) if tuesday else ' ', sep=', ')
print(*sorted(wednesday) if wednesday else ' ', sep=', ')
print(*sorted(thursday) if thursday else ' ', sep=', ')
print(*sorted(friday) if friday else ' ', sep=', ')
print(*sorted(saturday) if saturday else ' ', sep=', ')
print(*sorted(sunday) if sunday else ' ', sep=', ')