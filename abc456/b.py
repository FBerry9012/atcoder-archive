one = list(map(int, input().split()))
two = list(map(int, input().split()))
three = list(map(int, input().split()))

count = 0
for i in range(6):
    for j in range(6):
        for k in range(6):
            L = [one[i], two[j], three[k]]
            if set(L) == {4, 5, 6}:
                count += 1

ans = count / 216
print(ans)
