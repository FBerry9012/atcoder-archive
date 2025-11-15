X = int(input())

L = list(str(X))
L.sort()
for i, d in enumerate(L):
    if d != "0":
        n = L.pop(i)
        L.insert(0, n)
        break

print("".join(L))
