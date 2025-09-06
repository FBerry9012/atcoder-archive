import math

a, b = map(int, input().split())
c = a / b
# print (c)
d = math.floor(c)
# print (d)

e = c - d
f = d + 1 - c

# print (e)
# print (f)

if e > f:
    print(d + 1)
else:
    print(d)
