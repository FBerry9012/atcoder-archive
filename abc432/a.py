L = list(map(int, input().split()))
L.sort(reverse=True)
print("".join(map(str, L)))
