# https://www.acmicpc.net/problem/2234
# 비트마스킹과 bfs를 사용해 문제를 해결한다.
def check_wall(i, r, c):
    if len(bin(board[r][c])[2:]) >= i:
        return bin(board[r][c])[2:][-i]
    return '0'

def bfs(r, c, num):
    queue = deque([])
    queue.append([r, c])
    visited[r][c] = num
    union[num] = 1
    while queue:
        r, c = queue.popleft()
        for i, step in enumerate([[0, -1], [-1, 0], [0, 1], [1, 0]]):
            dr, dc = step
            if (check_wall(i+1, r, c) == '0') and visited[r+dr][c+dc] == -1:
                visited[r+dr][c+dc] = num
                queue.append([r+dr, c+dc])
                union[num] += 1

def add_union(r, c):
    result = union[visited[r][c]]
    for i, step in enumerate([[0, -1], [-1, 0], [0, 1], [1, 0]]):
        dr, dc = step
        if (check_wall(i+1, r, c) == '1') and 0<=r+dr<m and 0<=c+dc<n and visited[r+dr][c+dc] != visited[r][c]:
            result = max(result, union[visited[r+dr][c+dc]] + union[visited[r][c]])
    return result

from collections import deque
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
visited = [[-1 for _ in range(n)] for _ in range(m)] # 집합 체크
union = {}
num = 0
for r in range(m):
    for c in range(n):
        if visited[r][c] == -1:
            num += 1
            bfs(r, c, num)

max_size = 0
for r in range(m):
    for c in range(n):
        max_size = max(max_size, add_union(r, c))

print(num)
print(max(union.values()))
print(max_size)