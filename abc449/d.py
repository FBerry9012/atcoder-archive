def mt(X, Y):
    if X < 0 or Y < 0:
        return 0
    if X > Y:
        X, Y = Y, X
    m = X // 2
    ans = 2 * m * (m + 1) + (m + 1)
    y = (Y // 2) - (X // 2)
    ans += y * (X + 1)

    return ans


def f(L, R, D, U):
    return mt(R, U) - mt(L - 1, U) - mt(R, D - 1) + mt(L - 1, D - 1)


L, R, D, U = map(int, input().split())
ans = f(max(0, L), R, max(0, D), U)

if L < 0:
    ans += f(max(1, -R), -L, max(0, D), U)

if D < 0:
    ans += f(max(0, L), R, max(1, -U), -D)

if L < 0 and D < 0:
    ans += f(max(1, -R), -L, max(1, -U), -D)

print(ans)
