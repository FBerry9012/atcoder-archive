N, M = map(int, input().split())
S = input()
takahashi = set(S)
T = input()
aoki = set(T)
Q = int(input())

for i in range(Q):
    w = input()
    if not set(w).issubset(takahashi):
        print("Aoki")
    elif not set(w).issubset(aoki):
        print("Takahashi")
    else:
        print("Unknown")
