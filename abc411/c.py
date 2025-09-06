N, Q = map(int, input().split())
L = list(map(int, input().split()))
board = [0] * N
count = 0

for A in L:
    i = A - 1

    if board[i] == 0:
        board[i] = 1
        le = board[i - 1] if i - 1 >= 0 else 0
        ri = board[i + 1] if i + 1 < N else 0

        if le == 0 and ri == 0:
            count += 1
        elif le == 1 and ri == 1:
            count -= 1
    else:
        board[i] = 0

        le = board[i - 1] if i - 1 >= 0 else 0
        ri = board[i + 1] if i + 1 < N else 0

        if le == 0 and ri == 0:
            count -= 1
        elif le == 1 and ri == 1:
            count += 1

    print(count)
