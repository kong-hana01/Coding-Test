board = [list(map(int, input().split())) for _ in range(9)]
result = -1
for i in range(9):
    for j in range(9):
        if result < board[i][j]:
            result = board[i][j]
            row = i + 1
            col = j + 1
print(result)
print(row, col)