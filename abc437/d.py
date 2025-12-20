import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

B.sort()
pref = [0] * (M + 1)
for i in range(M):
    pref[i + 1] = pref[i] + B[i]

total = 0

for a in A:
    k = bisect.bisect_left(B, a)
    lower = (k * a) - pref[k]
    higher = (pref[M] - pref[k]) - (M - k) * a
    total += lower + higher

print(total % 998244353)
