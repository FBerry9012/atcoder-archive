N, M = map(int, input().split())
drink = [True] * M
for i in range(N):
    L = int(input())
    X = list(map(int, input().split()))
    for j in range(L):
        idx = X[j] - 1
        if drink[idx]:
            print(idx + 1)
            drink[idx] = False
            break
    else:
        print(0)
