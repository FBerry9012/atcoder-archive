N, M = map(int, input().split())
S = input()
T = input()
L = []


for i in range(0, N - M + 1):
    steps = 0
    for n in range(M):
        steps += (int(S[i + n]) - int(T[n])) % 10
    L.append(steps)

print(min(L))
