s = input()
a = len(s)
c = 0
# print (a)
for i in range(0, a - 1):
    j = i + 1
    k = int(s[i])
    l = int(s[j])
    b = k - l
    d = b % 10
    c = c + d

# print (c)
e = c + a + int(s[a - 1])
print(e)
