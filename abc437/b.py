from collections import defaultdict

H, W, N = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(H)]

counts = [0] * H
dic = defaultdict(set)
for r in range(H):
    for val in grid[r]:
        dic[val].add(r)

for _ in range(N):
    A = int(input())
    rows = dic.get(A, set())
    for r in rows:
        counts[r] += 1

print(max(counts))
