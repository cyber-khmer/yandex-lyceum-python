colors = []
while (color := input()) and len(color) <= 15:
    colors.append(color)

bad_color = input()

for color in colors:
    if color == bad_color:
        colors.remove(color)

print(colors)