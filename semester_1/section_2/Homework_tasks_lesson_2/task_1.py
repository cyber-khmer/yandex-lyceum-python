n = int(input())
flowers = []
for _ in range(n):
    flowers.append(input())

bad_substr = input()
for flower in flowers[:]:
    if bad_substr in flower:
        flowers.remove(flower)

print(*flowers, sep=', ')