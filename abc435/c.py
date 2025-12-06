N = int(input())
A = list(map(int, input().split()))

farthest = 0
for i in range(N):
    farthest = max(A[i] + i - 1, farthest)
    if farthest < i + 1:
        break


print(min(farthest + 1, N))
