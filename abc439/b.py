N = int(input())

dup = set()
while N != 1 and N not in dup:
    dup.add(N)
    N = sum(int(dig) ** 2 for dig in str(N))

if N == 1:
    print("Yes")
else:
    print("No")
