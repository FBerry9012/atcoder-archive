N = int(input())

MS = [[0] * N for _ in range(N)]
MS[0][(N - 1) // 2] = 1
last = (0, (N - 1) // 2)

for i in range(2, N**2 + 1):
    if MS[(last[0] - 1) % N][(last[1] + 1) % N] == 0:
        MS[(last[0] - 1) % N][(last[1] + 1) % N] = i
        last = ((last[0] - 1) % N, (last[1] + 1) % N)
    else:
        MS[(last[0] + 1) % N][last[1]] = i
        last = ((last[0] + 1) % N, last[1])

for row in MS:
    print(*row)
