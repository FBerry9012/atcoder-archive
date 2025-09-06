N, M= map(int, input().split())
S = input()
T = input()
D = [0] * (N + 2)

for _ in range (M):
    L, R = map(int, input().split())
    D[L] += 1
    D[R+1] -= 1

A = [0]*(N+1)
for i in range(1, N+1):
    A[i] = A[i-1] + D[i]
    
ans = []

for i in range(1, N+1):
    if A[i] % 2 == 0:
        ans.append(S[i-1])
    else:
        ans.append(T[i-1])
        
print("".join(ans))
