L = []
count = 0
A = int(input())
N = int(input())

max_length = len(str(N))
for length in range(1, max_length + 1):
    half_length = (length + 1) // 2
    for moto in range(10 ** (half_length - 1), 10**half_length):
        s = str(moto)
        if length % 2 == 0:
            kai_str = s + s[::-1]
        else:
            kai_str = s + s[-2::-1]

        kai_num = int(kai_str)
        if kai_num <= N:
            L.append(kai_num)
        else:
            break

L_length = len(L)
for j in range(L_length):
    temp = []
    n = L[j]
    while n > 0:
        temp.append(n % A)
        n = n // A
    if temp == temp[::-1]:
        count += L[j]

print(count)
