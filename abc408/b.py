N = int(input())
L = list(map(int, input().split()))
R = []

L.sort()

while len(L) >= 2:
    if L[0] == L[1]:
        L.pop(0)
    else:
        R.append(L[0])
        L.pop(0)

R.append(L[0])

print(len(R))
print(" ".join(map(str, R)))
