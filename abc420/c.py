N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = sum(min(a, b) for a, b in zip(A, B))

for _ in range(Q):
    c, x, v = input().split()
    x = int(x) - 1
    v = int(v)

    ans -= min(A[x], B[x])
    
    if c == "A":
        A[x] = v
    else:
        B[x] = v

    ans += min(A[x], B[x])
    
    print(ans)