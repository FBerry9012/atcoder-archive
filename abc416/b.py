S = input()
ans = []
val = 0
N = len(S)

for i in range(N):
    if val == 0:
        if S[i] == ".":
            ans.append("o")
            val += 1
        else:
            ans.append("#")
    else:
        if S[i] == ".":
            if S[i - 1] == "#":
                ans.append("o")
            else:
                ans.append(".")
        else:
            ans.append("#")

print("".join(ans))
