step = int(input())
s = input()
for i in range(0, len(s), step):
    print(s[i:i+step][::-1].capitalize(), end='')