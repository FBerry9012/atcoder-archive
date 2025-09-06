N = int(input())
Rmax = 0
Rmin = 10**10
Cmax = 0
Cmin = 10**10

for _ in range(N):
    R, C = map(int, input().split())
    if Rmax < R:
        Rmax = R
    if Rmin > R:
        Rmin = R
    if Cmax < C:
        Cmax = C
    if Cmin > C:
        Cmin = C

A = (Cmax - Cmin + 1) // 2
B = (Rmax - Rmin + 1) // 2

print(max(A, B))
