N = int(input())
W, H, B = [], [], []
for _ in range(N):
    w, h, b = map(int, input().split())
    W.append(w)
    H.append(h)
    B.append(b)


sumW = sum(W)
offset = sumW
dp = [-float("inf")] * (2 * sumW + 1)
dp[offset] = 0

for i in range(N):
    ndp = [-float("inf")] * (2 * sumW + 1)
    for d in range(2 * sumW + 1):
        if dp[d] == -float("inf"):
            continue
        else:
            ndp[d + W[i]] = max(ndp[d + W[i]], dp[d] + H[i])
            ndp[d - W[i]] = max(ndp[d - W[i]], dp[d] + B[i])
    dp = ndp

ans = max(dp[: offset + 1])
print(ans)

# TLE
