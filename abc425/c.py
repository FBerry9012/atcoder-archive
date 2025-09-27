N, Q = map(int, input().split())
L = list(map(int, input().split()))

prefix = [0] * (N + 1)
for i in range(N):
    prefix[i + 1] = prefix[i] + L[i]

idx = 0
for _ in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        idx = (idx + query[1]) % N
    else:
        l = query[1] - 1
        r = query[2] - 1
        lidx = (l + idx) % N
        ridx = (r + idx) % N

        if lidx <= ridx:
            total = prefix[ridx + 1] - prefix[lidx]
        else:
            total = (prefix[N] - prefix[lidx]) + prefix[ridx + 1]

        print(total)
