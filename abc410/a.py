N = int(input())
l = list(map(int, input().split()))
K = int(input())

count = sum(1 for x in l if x >= K)
print(count)
