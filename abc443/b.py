import math

N, K = map(int, input().split())
f = (-(2 * N - 1) + ((2 * N - 1) ** 2 + 8 * K) ** (1 / 2)) / 2
ans = math.ceil(f) - 1
print(ans)
