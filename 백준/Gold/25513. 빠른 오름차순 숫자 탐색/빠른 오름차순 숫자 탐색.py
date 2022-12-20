# https://www.acmicpc.net/problem/25513
# 접근 방법
# 주어진 요구사항대로 BFS를 사용해 문제를 해곃한다.
def bfs(r, c):
    visited = [[-1 for _ in range(5)] for _ in range(5)]
    queue = deque([])
    queue.append([r, c])
    target = board[r][c] + 1
    visited[r][c] = 0
    while queue:
        r, c = queue.popleft()
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if 0<=r+dr<5 and 0<=c+dc<5 and board[r+dr][c+dc] != -1 and visited[r+dr][c+dc] == -1:
                visited[r+dr][c+dc] = visited[r][c] + 1
                queue.append([r+dr, c+dc])
                if board[r+dr][c+dc] == target:
                    return [visited[r+dr][c+dc], r+dr, c+dc]
    return [-1, -1, -1]

from collections import deque
board = [list(map(int, input().split())) for _ in range(5)]
r, c = map(int, input().split())
cnt = 0
for i in range(6):
    result = bfs(r, c)
    if result[0] == -1:
        cnt = -1
        break
    cnt += result[0]
    r, c = result[1:]
print(cnt)