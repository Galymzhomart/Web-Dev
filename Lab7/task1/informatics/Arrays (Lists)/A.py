# №63. A[0], A[2], A[4], ...
n = int(input())
a = list(map(int, input().split()))

for i in range(0, n, 2):
    print(a[i], end=' ')