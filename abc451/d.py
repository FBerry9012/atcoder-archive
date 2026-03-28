import heapq

N = int(input())
bank = [str(2**i) for i in range(30)]
L = []
visited = set()
for a in bank:
    val = int(a)
    if val <= 10**9:
        heapq.heappush(L, val)
        visited.add(val)

count = 0
while L:
    current = heapq.heappop(L)
    count += 1
    if count == N:
        print(current)
        exit()

    cu_str = str(current)
    for a in bank:
        if len(cu_str) + len(a) > 10:
            continue
        new = int(cu_str + a)
        if new <= 10**9 and new not in visited:
            heapq.heappush(L, new)
            visited.add(new)
