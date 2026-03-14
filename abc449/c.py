from collections import Counter, deque

N, L, R = map(int, input().split())
S = input()

que = deque()
counts = Counter()
ans = 0

for i in range(N):
    idx = i - L
    if idx >= 0:
        add = S[idx]
        que.append(add)
        counts[add] += 1

    if len(que) > (R - L + 1):
        remove = que.popleft()
        counts[remove] -= 1

    now = S[i]
    ans += counts[now]

print(ans)
