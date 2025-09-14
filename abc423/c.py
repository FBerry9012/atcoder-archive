N, R = map(int, input().split())
L = list(map(int, input().split()))

left = 0
right = 0
for x in L[:R]:
    if x == 1:
        left += 1
    else:
        break

for x in reversed(L[R:]):
    if x == 1:
        right += 1
    else:
        break

L2 = L[left:R] + L[R : len(L) - right]
ans = len(L2) + sum(L2)
print(ans)
