N = int(input())
L = []
longest = 0
for _ in range(N):
    S = input()
    L.append(S)
    longest = max(longest, len(S))

for i in range(N):
    k = (longest - len(L[i])) // 2
    print("." * k + L[i] + "." * k)
