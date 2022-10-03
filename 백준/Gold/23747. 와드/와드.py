# https://www.acmicpc.net/problem/23747
# 접근 방법
# BFS를 통해 방문처리를 한다.
def bfs(r, c):
    queue = deque([])
    queue.append([r, c])
    visited[r][c] = '.'
    while queue:
        r, c = queue.popleft()
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if 0<=r+dr<R and 0<=c+dc<C and board[r+dr][c+dc] == board[r][c] and visited[r+dr][c+dc] == '#':
                visited[r+dr][c+dc] = '.'
                queue.append([r+dr, c+dc])

import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
board = [[x for x in input()] for _ in range(R)]
visited = [['#' for _ in range(C)] for _ in range(R)]
hr, hc = map(int, input().split())
history = deque([])
temp = input()
for x in temp:
    history.append(x)

now = [hr-1, hc-1]
while history:
    r, c = now
    move = history.popleft()
    if move == 'W':
        bfs(r, c)
    elif move == 'U':
        # visited[r-1][c] = '.'
        now = [r-1, c]
    elif move == 'D':
        # visited[r+1][c] = '.'
        now = [r+1, c]
    elif move == 'L':
        # visited[r][c-1] = '.'
        now = [r, c-1]
    elif move == 'R':
        # visited[r][c+1] = '.'
        now = [r, c+1]

visited[r][c] = '.'
for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
    if 0<=r+dr<R and 0<=c+dc<C:
        visited[r+dr][c+dc] = '.'

for i in range(R):
    print(*visited[i], sep = '')