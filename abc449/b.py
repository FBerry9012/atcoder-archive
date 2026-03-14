H, W, Q = map(int, input().split())

nowH = H
nowW = W
for _ in range(Q):
    a, b = map(int, input().split())
    if a == 1:
        print(nowW * b)
        nowH -= b
    else:
        print(nowH * b)
        nowW -= b
