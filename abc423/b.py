N = int(input())
L = list(map(int, input().split()))

if max(L) == 0:
    print(0)
else:
    for i in range(N):
        if L[i] == 1:
            left = i
            break

    for j in range(N):
        if L[N - 1 - j] == 1:
            right = N - 1 - j
            break

    ans = right - left
    print(ans)
