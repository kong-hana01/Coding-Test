# https://www.acmicpc.net/problem/16469
# 접근 방법
# 세명에 대해 각각 bfs를 돌린 뒤, 모든 지점에 대해 최대 얼마의 시간이 걸렸는지 체크하고, 이 중 가장 적은 시점을 출력한다.
def bfs(idx, row, col, INF):
    visited[idx][row][col] = 0
    queue = deque([])
    queue.append([row, col])
    while queue:
        r, c = queue.popleft()
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if 0<=r+dr<R and 0<=c+dc<C and not maze[r+dr][c+dc] and visited[idx][r+dr][c+dc] == INF:
                queue.append([r+dr, c+dc])
                visited[idx][r+dr][c+dc] = visited[idx][r][c] + 1

import sys
from collections import deque
input = sys.stdin.readline
R, C = map(int, input().split())
maze = [[int(x) for x in input().rstrip()] for _ in range(R)]
villain = []
for _ in range(3):
    villain.append(list(map(int, input().split())))
INF = int(1e6)
visited = [[[INF for _ in range(C)] for _ in range(R)] for _ in range(3)]
for i in range(3):
    bfs(i, villain[i][0]-1, villain[i][1]-1, INF)

count = 0
result = INF
for r in range(R):
    for c in range(C):
        meet_time = max(visited[0][r][c], visited[1][r][c], visited[2][r][c])
        if meet_time < result:
            result = meet_time
            count = 1
        elif meet_time == result:
            count += 1

if result != INF:
    print(result)
    print(count)
else:
    print(-1)