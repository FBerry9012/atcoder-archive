N = int(input())
A = list(map(int, input().split()))

ans = N * (N - 1) // 2
for i in range(N - 1):
    for j in range(i + 1, N):
        for k in range(j - i + 1):
            if sum(A[i : j + 1]) % A[i + k] == 0:
                ans -= 1
                break

print(ans)
