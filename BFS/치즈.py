# https://www.acmicpc.net/problem/2638
# 접근 방법
# BFS를 통해 치즈가 녹아 없어지는 시간을 체크한다.
# 단 매 초마다 모든 공간을 탐색할 수 없으므로 공기와 맞닿은 치즈의 위치를 따로 저장해 해당 위치만 탐색한다.
from collections import deque
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
queue = deque([])
for r in range(n):
    for c in range(m):
        if board[r][c]:
            for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                if 0<=r+dr<=n-1 and 0<=c+dc<=m-1 and board[r+dr][c+dc] == 0:
                    queue.append([r, c, 0])
                    visited[r][c] = 1
                    break

while queue:
    r, c, t = queue.popleft()
    count = 0
    for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        if 0<=r+dr<=n-1 and 0<=c+dc<=m-1 and board[r+dr][c+dc] == 0:
            count += 1

    if count >= 2:
        board[r][c] = 0
        for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            if 0<=r+dr<=n-1 and 0<=c+dc<=m-1 and board[r+dr][c+dc] and not visited[r+dr][c+dc]:
                queue.append([r+dr, c+dc, t+1])
                visited[r+dr][c+dc] = 1
    else:
        queue.append([r, c, t+1])

print(board)
print(t)