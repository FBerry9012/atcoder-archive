N = int(input())

ans = 0
for _ in range(N):
    i = _ + 1
    x = (-1) ** i * i**3
    ans += x

print(ans)
