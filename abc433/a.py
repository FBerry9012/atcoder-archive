X, Y, Z = map(int, input().split())

if (Z * Y - X) % (1 - Z) != 0:
    print("No")
else:
    n = (Z * Y - X) / (1 - Z)
    if n < 0:
        print("No")
    elif Y + n == 0:
        print("No")
    else:
        print("Yes")
