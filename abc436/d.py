import sys
from collections import deque

input = sys.stdin.readline

H, W = map(int, input().split())
grid = [list(input().strip()) for _ in range(H)]

start_r, start_c = 0, 0
goal_r, goal_c = H - 1, W - 1
teleported = set()
alph = {}
for r in range(H):
    for c in range(W):
        cell = grid[r][c]
        if "a" <= cell <= "z":
            if cell not in alph:
                alph[cell] = []
            alph[cell].append((r, c))

dist = [[-1] * W for _ in range(H)]
queue = deque()

dist[start_r][start_c] = 0
queue.append((start_r, start_c))
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while queue:
    r, c = queue.popleft()
    if r == goal_r and c == goal_c:
        print(dist[r][c])
        exit()
    next = []
    cell = grid[r][c]
    if "a" <= cell <= "z":
        if cell not in teleported:
            rendez = alph[cell]
            for next_r, next_c in rendez:
                if (next_r, next_c) != (r, c):
                    next.append((next_r, next_c))
            teleported.add(cell)

    for dr, dc in directions:
        next.append((r + dr, c + dc))

    for next_r, next_c in next:
        if not (0 <= next_r < H and 0 <= next_c < W):
            continue

        if grid[next_r][next_c] == "#":
            continue

        if dist[next_r][next_c] == -1:
            dist[next_r][next_c] = dist[r][c] + 1
            queue.append((next_r, next_c))

print(-1)
