# https://www.acmicpc.net/problem/27211
# 접근 방법
# BFS를 돌린다.
def bfs(r, c):
    queue = deque([])
    queue.append([r, c])
    visited[r][c] = True
    while queue:
        r, c = queue.popleft()
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            next_r = r+dr
            next_c = c+dc
            if next_r == n:
                next_r = 0
            elif next_r == -1:
                next_r = n-1
            if next_c == m:
                next_c = 0
            elif next_c == -1:
                next_c = m-1
            if graph[next_r][next_c] == 0 and not visited[next_r][next_c]:
                visited[next_r][next_c] = True
                queue.append([next_r, next_c])
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
cnt = 0
for r in range(n):
    for c in range(m):
        if graph[r][c] == 0 and not visited[r][c]:
            bfs(r, c)
            cnt += 1
print(cnt)