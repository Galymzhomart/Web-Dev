# №3060 Точная степень двойки
n = int(input())

p = 1
while p < n:
    p *= 2

if p == n:
    print("YES")
else:
    print("NO")