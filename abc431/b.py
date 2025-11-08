X = int(input())
N = int(input())
W = list(map(int, input().split()))
Q = int(input())
stats = [0] * N
for _ in range(Q):
    P = int(input())
    idx = P - 1
    stats[idx] = 1 - stats[idx]
    mass = X + sum(a for a, b in zip(W, stats) if b)
    print(mass)
