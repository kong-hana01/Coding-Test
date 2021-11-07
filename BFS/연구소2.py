# https://www.acmicpc.net/problem/17141
# 접근 방법
# 조합을 통해 모든 경우에 수에 대해 BFS를 동작시킨다. 이후 바이러스를 퍼트리는 최소 시간을 출력한다.
from collections import deque
from itertools import combinations
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
virus = []
count = 0
for r in range(n):
    for c in range(n):
        if board[r][c] == 2:
            virus.append([r, c])
            count += 1
        elif board[r][c] == 0:
            count += 1

result = n**2
count -= m
for C in combinations(virus, m):
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    queue = deque([])
    min_count = count
    max_time = 0
    for e in C:
        queue.append(e)
        visited[e[0]][e[1]] = 0
    while queue:
        r, c = queue.popleft()
        for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            if 0<=r+dr<=n-1 and 0<=c+dc<=n-1 and board[r+dr][c+dc] != 1 and (visited[r+dr][c+dc] == -1 or visited[r+dr][c+dc] > visited[r][c] + 1):
                visited[r+dr][c+dc] = visited[r][c] + 1
                queue.append([r+dr, c+dc])
                min_count -= 1

    max_time = visited[r][c]
    if min_count == 0:
        result = min(max_time, result)
if result == n**2:
    print(-1)
else:    
    print(result)