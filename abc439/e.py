import bisect

N = int(input())
strings = []
for _ in range(N):
    A, B = map(int, input().split())
    strings.append((A, B))

strings.sort(key=lambda x: (x[0], -x[1]))
B_list = [a[1] for a in strings]

LIS = [B_list[0]]
for i in range(len(B_list)):
    if B_list[i] > LIS[-1]:
        LIS.append(B_list[i])
    else:
        LIS[bisect.bisect_left(LIS, B_list[i])] = B_list[i]

print(len(LIS))
