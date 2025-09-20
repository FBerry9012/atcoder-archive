N, M, K = map(int, input().split())
count = [0] * N
ans = []

for _ in range(K):
    A, B = map(int, input().split())
    idx = A - 1
    count[idx] += 1
    if count[idx] == M:
        ans.append(A)

print(" ".join(map(str, ans)))
