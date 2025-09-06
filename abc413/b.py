N = int(input())
L = [input().strip("\n") for i in range(N)]
R = []

for a in range(N):
    for b in range(N):
        if a == b:
            continue
        R.append(L[a] + L[b])

Dup = list(set(R))
print(len(Dup))
