N, M = map(int, input().split())
grid = [input().strip() for _ in range(N)]

kinds = set()
for i in range(N - M + 1):
    for j in range(N - M + 1):
        sub = "".join(row[j : j + M] for row in grid[i : i + M])
        kinds.add(sub)

print(len(kinds))
