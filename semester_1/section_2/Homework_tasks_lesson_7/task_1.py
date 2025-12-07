from collections import defaultdict

res = defaultdict(list)
while (s := input()) != '':
    calories, name = s.split()
    calories = int(calories)
    calories_category = calories // 200 * 200
    res[calories_category].append(name)

print({k: sorted(v) for k, v in res.items()})