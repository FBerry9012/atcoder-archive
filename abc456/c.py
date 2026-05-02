S = input()

ans = 0
streak = 0
last_char = None

for char in S:
    if char != last_char:
        streak += 1
    else:
        ans += (streak * (streak + 1)) // 2
        streak = 1

    last_char = char

ans += (streak * (streak + 1)) // 2
ans = ans % 998244353

print(ans)
