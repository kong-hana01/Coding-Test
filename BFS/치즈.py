# https://www.acmicpc.net/problem/2638
# 접근 방법
# BFS를 통해 치즈가 녹아 없어지는 시간을 체크한다.
# 단 매 초마다 모든 공간을 탐색할 수 없으므로 공기와 맞닿은 치즈의 위치를 따로 저장해 해당 위치만 탐색한다.
def dfs(r, c):
    if visited[r][c]:
        return 
    board[r][c] = -1
    visited[r][c] = 1
    for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        if 0<=r+dr<=n-1 and 0<=c+dc<=m-1 and not board[r+dr][c+dc] and not visited[r+dr][c+dc]:
            dfs(r+dr, c+dc)

from collections import deque
import sys
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
dfs(0, 0)

queue = deque([])
for r in range(n):
    for c in range(m):
        if board[r][c] == 1:
            queue.append([r, c, 0])


time = 0
while queue:
    check_air = []
    melting_cheese = []
    while queue and queue[0][2] == time:
        r, c, t = queue.popleft()
        count = 0
        temp = []
        for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            if 0<=r+dr<=n-1 and 0<=c+dc<=m-1:
                if board[r+dr][c+dc] == -1:
                    count += 1
                elif board[r+dr][c+dc] == 0:
                    temp.append([r+dr, c+dc])

        if count >= 2:
            melting_cheese.append([r, c])
            check_air = check_air + temp

        else:
            queue.append([r, c, t+1])
    

    for x in melting_cheese:
        board[x[0]][x[1]] = -1
    for x in check_air:
        dfs(x[0], x[1])
    
    time += 1

print(time)