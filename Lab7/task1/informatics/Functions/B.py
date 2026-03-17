# №307 Степень
def power(a, n):
    res = 1
    for _ in range(n):
        res *= a
    return res

a, n = input().split()
a = float(a)
n = int(n)

print(power(a, n))