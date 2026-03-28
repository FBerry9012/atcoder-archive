import heapq

L = []
Q = int(input())
for _ in range(Q):
    A, B = map(int, input().split())
    if A == 1:
        heapq.heappush(L, B)
    else:
        while L and L[0] <= B:
            heapq.heappop(L)
    print(len(L))
