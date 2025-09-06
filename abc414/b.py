N = int(input())
L = []

for i in range(N):
    line = input()
    c_str, l_str = line.split()
    c = c_str
    l = int(l_str)
    if len(L) + l > 100:
        print("Too Long")
        L = []
        break
    for j in range(l):
        L.append(c)

print("".join(L))
