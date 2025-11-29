T = int(input())
for _ in range(T):
    N, H = map(int, input().split())
    t, l, u = map(int, input().split())

    top = min(H + t, u)
    bot = max(H - t, l, 1)

    failed = top < bot

    tl = t
    for _ in range(N - 1):
        t, l, u = map(int, input().split())
        dt = t - tl
        top = min(top + dt, u)
        bot = max(bot - dt, l, 1)
        tl = t
        if top < bot:
            failed = True
    print("No" if failed else "Yes")
