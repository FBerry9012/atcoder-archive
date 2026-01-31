T = int(input())
for _ in range(T):
    N = int(input())
    R = list(map(int, input().split()))
    copy = list(R)
    for i in range(1, N):
        copy[i] = min(copy[i], copy[i - 1] + 1)
    for i in range(N - 2, -1, -1):
        copy[i] = min(copy[i], copy[i + 1] + 1)
    ans = 0
    for i in range(N):
        ans += R[i] - copy[i]
    print(ans)
