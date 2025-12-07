s1, s2 = input().lower(), input().lower()
if s1.count('a') > s2.count('a'):
    print(True)
elif s1.count('a') <= s2.count('a') and len(s1) > len(s2):
    print(True)
elif s1.count('a') <= s2.count('a') and len(s1) <= len(s2) and s1[::-1] > s2[::-1]:
    print(True)
else:
    print(False)