import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dic = {}
ans = 0
for x in A:
    dic[x] = dic.get(x - 1, 0) + 1
    if dic[x] > ans:
        ans = dic[x]

print(ans)
