n = int(input())
things = {}
for i in range(n):
    creature, *thing = input().split()
    thing = ' '.join(thing)
    things[creature] = max(things.get(creature, ''), thing, key=len)

print(things)