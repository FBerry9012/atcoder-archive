N, T = map(int, input().split())
A = list(map(int, input().split()))

flag = 0
last_time = 0
if N == 0:
    print(T)
    exit()
for i in range(N):
    if i == 0:
        flag += 1
        last_time = A[i]
    else:
        if A[i] - last_time > 100:
            flag += 1
            last_time = A[i]

if T - last_time > 100:
    ans = T - (flag * 100)
else:
    ans = T - ((flag - 1) * 100 + T - last_time)

print(ans)
