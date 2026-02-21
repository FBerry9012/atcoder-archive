M, A, B = map(int, input().split())

inv = [[0] * M for _ in range(M)]
ans = 0
for x in range(M):
    for y in range(M):
        if inv[x][y] != 0:
            continue
        path = []
        current_x, current_y = x, y
        found = False

        while inv[current_x][current_y] == 0:
            path.append((current_x, current_y))
            inv[current_x][current_y] = -1
            if current_x == 0 or current_y == 0:
                found = True
                break
            nex = (A * current_y + B * current_x) % M
            current_x, current_y = current_y, nex
            if inv[current_x][current_y] == 1:
                found = True
                break
            elif inv[current_x][current_y] == 2:
                found = False
                break
            elif inv[current_x][current_y] == -1:
                found = False
                break
        if found:
            a = 1
        else:
            a = 2
        for n, m in path:
            inv[n][m] = a

ans = sum(row.count(2) for row in inv)
print(ans)
