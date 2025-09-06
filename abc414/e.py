N = int(input())
total = (N * (N + 1)) // 2

a = 0
i = 1
while i <= N:
    q = N // i
    j = N // q + 1
    a += (j - i) * q
    i = j

raw_ans = total - a
ans = raw_ans % 998244353
print(ans)
