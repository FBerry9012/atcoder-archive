import numpy as np

N, M = map(int, input().split())
diff = np.zeros(N + 2, dtype=int)
for i in range(M):
    l, r = map(int, input().split())
    diff[l] += 1
    diff[r + 1] -= 1

count = np.cumsum(diff[1 : N + 1])

print(np.min(count))
