P, Q = map(int, input().split())
X, Y = map(int, input().split())

if 100 > X - P >= 0 and 100 > Y - Q >= 0:
    print("Yes")
else:
    print("No")
