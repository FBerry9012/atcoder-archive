import bisect

N, A, B = map(int, input().split())
S = input()

ans = 0
l = 0

a_prefix = [0] * (N + 1)
b_prefix = [0] * (N + 1)
for index, value in enumerate(S):
    a_prefix[index + 1] = a_prefix[index] + (value == "a")
    b_prefix[index + 1] = b_prefix[index] + (value == "b")

for r in range(N):
    while b_prefix[r + 1] - b_prefix[l] >= B:
        l += 1
    thre = a_prefix[r + 1] - A
    idx = bisect.bisect_right(a_prefix, thre, l, r + 1)
    ans += idx - l

print(ans)
