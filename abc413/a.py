N, M = map(int, input().split())
L = list(map(int, input().split()))

SUM = sum(L)
if M >= SUM:
    print("Yes")
else:
    print("No")
