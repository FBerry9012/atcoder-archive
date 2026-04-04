H, W = map(int, input().split())

A = ["#" for _ in range(W)]
B = ["#"] + ["."] * (W - 2) + ["#"]

print("".join(A))
for _ in range(H - 2):
    print("".join(B))
print("".join(A))
