S = input()

a = 0
ab = 0
ans = 0

for cha in S:
    if cha == "A":
        a += 1
    elif cha == "B":
        if a > 0:
            ab += 1
            a -= 1
    elif cha == "C":
        if ab > 0:
            ans += 1
            ab -= 1

print(ans)
