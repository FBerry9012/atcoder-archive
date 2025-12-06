from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    X, Y = map(int, input().split())
    graph[Y - 1].append(X - 1)

Q = int(input())
black = [False] * N
reachable = [False] * N
for _ in range(Q):
    type, migawari = map(int, input().split())
    v = migawari - 1
    if type == 1:
        if black[v]:
            continue
        black[v] = True
        if reachable[v]:
            continue
        q = deque([v])
        reachable[v] = True
        while q:
            u = q.popleft()
            for w in graph[u]:
                if not reachable[w]:
                    reachable[w] = True
                    q.append(w)
    else:
        if reachable[v]:
            print("Yes")
        else:
            print("No")
