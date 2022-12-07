# https://www.acmicpc.net/problem/16946
# 접근 방법
# 모든 빈칸에 대해 이동할 수 있는 칸의 수를 더한 뒤, 1이 위치한 곳의 상하좌우에 대한 이동할 수 있는 칸의 범위를 구해 답을 구한다.
def bfs(r, c, union_number):
    queue = deque([])
    queue.append([r, c])
    visited[r][c] = union_number
    cnt_of_union[union_number] = 1
    while queue:
        r, c = queue.popleft()
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if 0<=r+dr<n and 0<=c+dc<m and visited[r+dr][c+dc] == -1 and board[r+dr][c+dc] == 0:
                visited[r+dr][c+dc] = union_number
                cnt_of_union[union_number] += 1
                queue.append([r+dr, c+dc])
    
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
board = [[int(x) for x in input().rstrip()] for _ in range(n)]
visited = [[-1 for _ in range(m)] for _ in range(n)]
result = [["0" for _ in range(m)] for _ in range(n)]
cnt_of_union = {}

wall = []
union_number = 1
for r in range(n):
    for c in range(m):
        if board[r][c]:
            wall.append([r, c])
        else:
            if visited[r][c] == -1:
                bfs(r, c, union_number)
                union_number += 1

for r, c in wall:
    cnt = 1
    adj_union_set = set([])
    for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        if 0<=r+dr<n and 0<=c+dc<m and board[r+dr][c+dc] == 0:
            adj_union_set.add(visited[r+dr][c+dc])
    
    for union in adj_union_set:
        cnt += cnt_of_union[union]
    
    result[r][c] = str(cnt % 10)

for x in result:
    print("".join(x))