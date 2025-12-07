s = input().split()
summa = [ord(j) for i in s for j in i if j.isalpha()]
print(sum(summa))