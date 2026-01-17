import sys

input = sys.stdin.readline
N, M, L, S, T = map(int, input().split())
ad = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, c = map(int, input().split())
    ad[u].append((v, c))

ans = set()
stack = [(1, 0, 0)]

while stack:
    u, steps, costs = stack.pop()
    if steps == L:
        if S <= costs <= T:
            ans.add(u)
        continue
    for v, c in ad[u]:
        newcosts = costs + c
        if newcosts <= T:
            stack.append((v, steps + 1, newcosts))

print(*(sorted(ans)))
