N = int(input())
L = list(map(int, input().split()))
ans = [0] * (N - 1)

ans[0] = L[0]
for i in range(1, N - 1):
    ans[i] = L[i] + ans[i - 1]

print(" ".join(map(str, ans)))

while len(ans) > 1:
    K = ans[0]
    ans = [x - K for x in ans]
    ans = [x for x in ans if x != 0]
    print(" ".join(map(str, ans)))
