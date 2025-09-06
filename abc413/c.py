import sys

input = sys.stdin.readline
from collections import deque

Q = int(input())
L = deque()

for i in range(Q):
    A, *B = map(int, input().split())

    if A == 1:
        c, x = B
        lil = [c, x]
        L.append(lil)

    else:
        k = B[0]
        output = 0
        while k > 0:
            y, z = L[0]
            take = min(y, k)
            output += z * take
            k -= take
            y -= take

            if y > 0:
                L[0] = [y, z]
            else:
                L.popleft()
        print(output)
