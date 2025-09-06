a, b = map(int, input().split())
L = list(map(int, input().split()))

L.insert(0, 0)

for i in range(0, a + 1):
    if L[i] - L[i - 1] > b:
        print("No")
        break
else:
    print("Yes")
