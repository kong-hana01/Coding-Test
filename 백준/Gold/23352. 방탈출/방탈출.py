# https://www.acmicpc.net/problem/23352
# 접근 방법
# 모든 케이스에 대해 BFS를 적용하여 문제를 해결한다.
def bfs(r, c):
    global lengthOfPath, result
    startNum = maze[r][c]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[r][c] = 1
    queue = deque([])
    queue.append([r, c])
    while queue:
        r, c = queue.popleft()
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if 0<=r+dr<n and 0<=c+dc<m and maze[r+dr][c+dc] != 0 and not visited[r+dr][c+dc]:
                queue.append([r+dr, c+dc])
                visited[r+dr][c+dc] = visited[r][c] + 1
                if visited[r+dr][c+dc] > lengthOfPath:
                    result = maze[r+dr][c+dc] + startNum
                    lengthOfPath = visited[r+dr][c+dc]
                elif visited[r+dr][c+dc] == lengthOfPath:
                    result = max(result, maze[r+dr][c+dc] + startNum)

from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
result = 0
lengthOfPath = 0
for r in range(n):
    for c in range(m):
        if maze[r][c] > 0:
            bfs(r, c)
print(result)
