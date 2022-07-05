# https://www.acmicpc.net/problem/21938
# 접근 방법
# BFS를 사용해 문제를 해결한다.
from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
pixel = [[0 for _ in range(m)] for _ in range(n)]
Temp = [list(map(int, input().split())) for _ in range(n)]
t = int(input())
for r in range(n):
    temp = Temp[r]
    for c in range(m):
        pixel[r][c] = 1 if (temp[c * 3] + temp[c * 3 + 1] + temp[c * 3 + 2]) / 3 >= t else 0
visited = [[False for _ in range(m)] for _ in range(n)]
cnt = 0
for r in range(n):
    for c in range(m):
        if not visited[r][c] and pixel[r][c]:
            queue = deque([])
            queue.append([r, c])
            visited[r][c] = True
            while queue:
                x, y = queue.popleft()
                for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    if 0<=x+dx<n and 0<=y+dy<m and not visited[x+dx][y+dy] and pixel[x+dx][y+dy]:
                        visited[x+dx][y+dy] = True
                        queue.append([x+dx, y+dy])
            cnt += 1
print(cnt)
