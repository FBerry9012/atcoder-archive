N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

INF = 10**10
dp1 = -INF
dp2 = -INF
dp3 = -INF
current = 0
for i in range(N):
    if i == 0:
        next_dp1 = A[0]
    else:
        next_dp1 = dp1 + A[i]

    if i >= 1:
        next_dp2 = max(dp1 + B[i], dp2 + B[i])
    else:
        next_dp2 = -INF

    if i >= 2:
        next_dp3 = max(dp2 + C[i], dp3 + C[i])
    else:
        next_dp3 = -INF

    dp1, dp2, dp3 = next_dp1, next_dp2, next_dp3

print(dp3)
