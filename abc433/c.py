S = str(input())
N = len(S)
ans = 0
i = 0

blocks = []
i = 0
while i < N:
    d = S[i]
    j = i
    while j < N and S[j] == d:
        j += 1
    blocks.append((int(d), j - i))
    i = j

ans = 0

i = 0
while i < len(blocks) - 1:
    df, lenf = blocks[i]
    dl, lenl = blocks[i + 1]

    if dl - df == 1:
        m = min(lenf, lenl)
        ans += m
    i += 1

print(ans)
