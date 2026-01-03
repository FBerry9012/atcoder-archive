import math

N = int(input())

count = [0] * (N + 1)
ymax = int(math.sqrt(N))

for x in range(1, ymax + 1):
    for y in range(x + 1, ymax + 1):
        s = (x**2) + (y**2)
        if s > N:
            break
        count[s] += 1

ans = [a for a, b in enumerate(count) if b == 1]

print(len(ans))
print(" ".join(map(str, ans)))
