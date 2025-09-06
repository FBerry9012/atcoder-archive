a, b = map(int, input().split())
c = 0
for d in range(1, 7):
    for e in range(1, 7):
        if d + e >= a:
            c = c + 1
        elif abs(d - e) >= b:
            c = c + 1

print(c / 36)
