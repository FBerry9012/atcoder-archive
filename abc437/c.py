T = int(input())

for _ in range(T):
    N = int(input())

    costs = []
    total = 0

    for _ in range(N):
        weight, power = map(int, input().split())
        costs.append(weight + power)
        total += power

    costs.sort()
    ans = 0
    current_cost = 0

    for cost in costs:
        if current_cost + cost <= total:
            current_cost += cost
            ans += 1
        else:
            break

    print(ans)
