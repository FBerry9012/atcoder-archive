from scipy.spatial import distance

N, M = map(int, input().split())
Ss = [input() for _ in range(N)]

thre = N // 2
L = []

for i in range(M):
    count = sum(1 for j in range(N) if Ss[j][i] == "1")
    if count > thre:
        L.append(0)
    else:
        L.append(1)

dist = []
for j in range(N):
    b = [int(c) for c in Ss[j]]
    dist.append(distance.hamming(L, b) * M)

mi = min(dist)
banme = [str(i+1) for i, v in enumerate(dist) if v == mi]
print(" ".join(banme))