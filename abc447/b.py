S = input()
counts = {}
for a in S:
    counts[a] = counts.get(a, 0) + 1

max_count = max(counts.values())
remove = {a for a, count in counts.items() if count == max_count}

print("".join(a for a in S if a not in remove))
