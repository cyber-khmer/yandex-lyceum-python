from _collections import defaultdict

n = int(input())
subject_marks = defaultdict(list)
for _ in range(n):
    s = input().split(': ')
    subject_marks[s[0]].append(int(s[1]))

print(dict(subject_marks))