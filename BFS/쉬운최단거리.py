# https://www.acmicpc.net/problem/14940
# 접근 방법
# 0. 목표지점에서 다른 지점까지 BFS를 통해 거리를 갱신한다.
# 1. 이후 출력 조건에 맞게 출력한다.
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)] 
visited = [[-1 for _ in range(m)] for _ in range(n)]
queue = deque([])
for r in range(n):
    for c in range(m):
        if board[r][c] == 2:
            queue.append([r, c])
            visited[r][c] = 0
        elif board[r][c] == 0:
            visited[r][c] = 0


while queue:
    r, c = queue.popleft()
    for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        if 0<=r+dr<n and 0<=c+dc<m and visited[r+dr][c+dc] == -1:
            if board[r+dr][c+dc] == 1:
                visited[r+dr][c+dc] = visited[r][c] + 1
                queue.append([r+dr, c+dc])

for r in range(n):
    for c in range(m):
        print(visited[r][c], end=' ')
    print()