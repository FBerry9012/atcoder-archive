X, C = map(int, input().split())

Y = X / ((1000 + C) / 1000)
ans = (Y // 1000) * 1000
print(int(ans))
