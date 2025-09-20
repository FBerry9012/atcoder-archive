from collections import deque

N = int(input())
skill = [[] for _ in range(N)]
root = []

for i in range(N):
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        root.append(i)
    else:
        if A != 0:
            skill[A - 1].append(i)
        if B != 0:
            skill[B - 1].append(i)

master = [False] * (N)
q = deque()

for n in root:
    master[n] = True
    q.append(n)

while q:
    current = q.popleft()
    for next in skill[current]:
        if not master[next]:
            master[next] = True
            q.append(next)

print(sum(master))
