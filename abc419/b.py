Q = int(input())
L = []

for _ in range(Q):
    que = input().strip()
    if que.startswith("1"):
        i,x = que.split()
        L.append(int(x))
        
    else:
        m = min(L)
        L.remove(m)
        print(m)
