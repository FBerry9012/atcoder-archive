from collections import Counter

N = int(input())
A = list(map(int, input().split()))

count = Counter(A)
dup = [v for k, v in count.items() if v > 1]

ans = sum((v * (v - 1) // 2) * (N - v) for v in dup)

print(ans)
