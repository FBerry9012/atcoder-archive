S = input()
T = input()

i, j = 0, 0
ans = 0

while i < len(S) and j < len(T):
    if S[i] == T[j]:
        i += 1
        j += 1
    elif S[i] == "A":
        i += 1
        ans += 1
    elif T[j] == "A":
        j += 1
        ans += 1
    else:
        print(-1)
        exit()

while i < len(S):
    if S[i] == "A":
        i += 1
        ans += 1
    else:
        print(-1)
        exit()

while j < len(T):
    if T[j] == "A":
        j += 1
        ans += 1
    else:
        print(-1)
        exit()

print(ans)
