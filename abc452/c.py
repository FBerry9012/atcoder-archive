N = int(input())

L = []
for i in range(N):
    A, B = map(int, input().split())
    L.append((A, B))

ava = [set() for _ in range(N)]
SS = []
M = int(input())
for _ in range(M):
    S = input()
    SS.append(S)
    for i in range(N):
        A = L[i][0]
        B = L[i][1]
        if len(S) == A:
            ava[i].add(S[B - 1])

for S in SS:
    if len(S) == N:
        for i in range(N):
            if S[i] not in ava[i]:
                print("No")
                break
        else:
            print("Yes")
    else:
        print("No")
