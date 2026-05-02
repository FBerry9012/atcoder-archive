S = input()
A = 0
B = 0
C = 0

for char in S:
    if char == "a":
        A = A + B + C + 1
    elif char == "b":
        B = A + B + C + 1
    else:
        C = A + B + C + 1

ans = (A + B + C) % 998244353
print(ans)
