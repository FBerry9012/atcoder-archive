import bisect
import sys
from collections import defaultdict

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))

pos = defaultdict(list)
for idx, val in enumerate(A):
    pos[val].append(idx)

ans = 0

for j, Aj in enumerate(A):
    if Aj % 5 != 0:
        continue

    n = Aj // 5
    Ai = 7 * n
    Ak = 3 * n

    if Ai in pos and Ak in pos:
        list_i = pos[Ai]
        list_k = pos[Ak]

        left_i = bisect.bisect_left(list_i, j)
        left_k = bisect.bisect_left(list_k, j)
        right_i = len(list_i) - left_i
        right_k = len(list_k) - left_k

        ans += left_i * left_k
        ans += right_i * right_k

print(ans)
