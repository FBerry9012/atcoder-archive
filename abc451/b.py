N, M = map(int, input().split())

L = [0] * M
for _ in range(N):
    A, B = map(int, input().split())
    L[A - 1] -= 1
    L[B - 1] += 1

print(*L, sep="\n")
