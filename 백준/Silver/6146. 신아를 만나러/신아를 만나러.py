# https://www.acmicpc.net/problem/6146
# 접근 방법
# 그래프에 웅덩이의 위치를 넣어 BFS를 돌리고 문제를 해결한다.
from collections import deque
x, y, n = map(int, input().split())
visited = [[-1 for _ in range(1001)] for _ in range(1001)]
for _ in range(n):
    a, b = map(lambda x: x+500, map(int, input().split()))
    visited[a][b] = 2000

queue = deque([])
queue.append([500, 500])
visited[500][500] = 0
while visited[x+500][y+500] == -1:
    r, c = queue.popleft()
    for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        if 0<=r+dr<=1000 and 0<=c+dc<=1000 and visited[r+dr][c+dc] == -1:
            queue.append([r+dr, c+dc])
            visited[r+dr][c+dc] = visited[r][c] + 1
print(visited[x+500][y+500])