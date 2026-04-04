S = input()
T = input()

n, m = len(S), len(T)
s = 0
deny = []
while s < n:
    t = 0
    curr_s = s
    while curr_s < n:
        if S[curr_s] == T[t]:
            t += 1
        if t == m:
            break
        curr_s += 1
    if t < m:
        break
    right = curr_s
    t = m - 1
    left = right
    while left >= 0:
        if S[left] == T[t]:
            t -= 1
        if t < 0:
            break
        left -= 1
    deny.append((left, right))

    s = left + 1

ans = 0
a = -1
b = 0
for r in range(n):
    while b < len(deny) and deny[b][1] == r:
        a = max(a, deny[b][0])
        b += 1
    count = r - a
    ans += count

print(ans)
