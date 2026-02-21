import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, D = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    ans = sum(A) - sum(B)
    Q = deque()
    for i in range(N):
        Q.append((i, A[i]))
        Q[0] = (Q[0][0], Q[0][1] - B[i])
        while Q[0][1] < 0:
            lack = Q[0][1]
            Q.popleft()
            Q[0] = (Q[0][0], Q[0][1] + lack)
        while i - Q[0][0] >= D:
            x = Q.popleft()
            ans -= x[1]
    print(ans)
