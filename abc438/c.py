N = int(input())
A = list(map(int, input().split()))

stack = []
for n in A:
    if stack and stack[-1][0] == n:
        stack[-1][1] += 1
        if stack[-1][1] == 4:
            stack.pop()
    else:
        stack.append([n, 1])
ans = sum(b for a, b in stack)
print(ans)
