N = int(input())
L = list(map(int, input().split()))

kind = set(n for n in L if n != -1)
if len(kind) != sum(1 for n in L if n != -1):
    print("No")
else:
    print("Yes")

    ans = []
    rest = iter(set(range(1, N + 1)) - kind)
    for n in L:
        if n == -1:
            ans.append(next(rest))
        else:
            ans.append(n)

    print(" ".join(map(str, ans)))
