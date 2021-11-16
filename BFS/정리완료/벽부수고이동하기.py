# https://www.acmicpc.net/problem/2206
# 접근 방법
# 벽을 한번도 부수지 않은 경우와 벽을 한번만 부순 경우의 방문 처리를 위한 리스트를 만든 뒤, 각각 다르게 취급하여 BFS를 동작시킨다.
def bfs(x, y):
    queue = deque([])
    queue.append([x, y, 0])
    visited[x][y] = [1, 1]
    while queue:
        r, c, count = queue.popleft()
        
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if 0<=r+dr<=n-1 and 0<=c+dc<=m-1:
                if board[r+dr][c+dc]:
                    if count == 1 or visited[r+dr][c+dc][1] <= visited[r][c][0] + 1:
                        continue
                    visited[r+dr][c+dc][1] = visited[r][c][0] + 1
                    queue.append([r+dr, c+dc, 1])
                    if r+dr == n-1 and c+dc == m-1:
                        return visited[r+dr][c+dc][1]

                else:
                    if visited[r+dr][c+dc][count] <= visited[r][c][count] + 1:
                        continue
                    visited[r+dr][c+dc][count] = visited[r][c][count] + 1
                    queue.append([r+dr, c+dc, count])
                    if r+dr == n-1 and c+dc == m-1:
                        return visited[r+dr][c+dc][count]

    return -1 if min(visited[n-1][m-1]) == INF else min(visited[n-1][m-1])

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [[int(x) for x in input().rstrip()] for _ in range(n)]
INF = int(1e9)
visited = [[[INF, INF] for _ in range(m)] for _ in range(n)]
result = bfs(0, 0)
print(result)