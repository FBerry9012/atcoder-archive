from itertools import product

N, K, X = map(int, input().split())
L = []

for i in range(N):
    L.append(input())

L.sort()

aholist = ["".join(p) for p in product(L, repeat=K)]

aholist.sort()
print(aholist[X - 1])
