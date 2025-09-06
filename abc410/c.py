N, Q = map(int, input().split())
l = [i for i in range(1, N + 1)]
a = 0

for _ in range(Q):
    Que = list(map(int, input().split()))

    if Que[0] == 1:
        b = (Que[1] - 1 + a) % N
        l[b] = Que[2]

    elif Que[0] == 2:
        b = (Que[1] - 1 + a) % N
        print(l[b])

    else:
        c = Que[1] % N
        a = (a + c) % N
