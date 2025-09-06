N, Q = map(int, input().split())
l = list(map(int, input().split()))
r = [0] * N
L = []

for i in range(Q):
    if l[i] >= 1:
        L.append(l[i])
        r[l[i] - 1] += 1
    else:
        m = min(r)
        n = r.index(m)
        L.append(n + 1)
        r[n] += 1

print(*L)
