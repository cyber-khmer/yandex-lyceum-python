n = int(input())
asteroids = {}
for i in range(n):
    r, name = input().split()
    r = int(r)
    asteroids[name] = asteroids.get(name, []) + [r]
for name in asteroids:
    asteroids[name] = [min(asteroids[name]), max(asteroids[name])]

print(asteroids)