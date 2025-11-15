N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

D = Y - X
r = A[0] * X % D
for i in range(1, N):
    if A[i] * X % D != r:
        print(-1)
        exit()

Wmin = max(A[i] * X for i in range(N))
Wmax = min(A[i] * Y for i in range(N))

W = Wmax - (Wmax - r) % D
if W < Wmin:
    print(-1)
    exit()

ans = sum((W - A[i] * X) // D for i in range(N))
print(ans)
