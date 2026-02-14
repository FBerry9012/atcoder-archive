N = int(input())
L = list(map(int, input().split()))

K = 10**100
ans = list(range(N))
leap = [x - 1 for x in L]

rest = K
while rest:
    if rest & 1:
        newans = [0] * N
        for i in range(N):
            newans[i] = leap[ans[i]]
        ans = newans
    newleap = [0] * N
    for i in range(N):
        newleap[i] = leap[leap[i]]
    leap = newleap
    rest >>= 1

print(*([x + 1 for x in ans]))
