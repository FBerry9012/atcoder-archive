N, M = map(int, input().split())
A = list(map(int, input().split()))

moddict = {}

for x in A:
    k = len(str(x))
    mod = x % M

    if k not in moddict:
        moddict[k] = {}
    if mod not in moddict[k]:
        moddict[k][mod] = 0

    moddict[k][mod] += 1

ans = 0

for x in A:
    for k in moddict:
        target = (-x * (10**k)) % M
        if target in moddict[k]:
            ans += moddict[k][target]

print(ans)
