n = int(input())
s = input().split()
print(*s[:len(s) - n])
print(*s[len(s) - n:])