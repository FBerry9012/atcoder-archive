N, M = map(int, input().split())
A = list(map(int, input().split()))

SUM = sum(A)
ap = SUM - M
if ap in A:
    print("Yes")
else:
    print("No")
