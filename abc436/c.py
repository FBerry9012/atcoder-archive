import sys

input = sys.stdin.readline
N, M = map(int, input().split())

placed = set()
ans = 0
for _ in range(M):
    R, C = map(int, input().split())
    judge = [(R, C), (R + 1, C), (R, C + 1), (R + 1, C + 1)]
    NG = any(cell in placed for cell in judge)
    if not NG:
        for cell in judge:
            placed.add(cell)
        ans += 1

print(ans)
