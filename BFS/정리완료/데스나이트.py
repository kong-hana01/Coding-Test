from collections import deque
n = int(input())
r1, c1, r2, c2 = map(int, input().split())
board = [[-1 for _ in range(n)] for _ in range(n)]
queue = deque([])
queue.append([r1, c1])
board[r1][c1] = 0
while board[r2][c2] == -1 and queue:
    r, c = queue.popleft()
    for dx, dy in [[-2, -1], [-2, 1], [0, -2], [0, 2], [2, -1], [2, 1]]:
        if 0<=r+dx<n and 0<=c+dy<n and board[r+dx][c+dy] == -1:
            board[r+dx][c+dy] = board[r][c] + 1
            queue.append([r+dx, c+dy])
print(board[r2][c2])