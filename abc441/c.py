N, K, X = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse=True)
S = [0] * (N + 1)
for i in range(N):
    S[i + 1] = S[i] + A[i]

for i in range(1, N + 1):
    j = K - (N - i)
    if j <= 0:
        a = 0
    else:
        a = S[i] - S[i - j]
    if a >= X:
        print(i)
        exit()

print("-1")
