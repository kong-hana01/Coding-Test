# https://www.acmicpc.net/problem/1926
# 접근 방법
# 주어진 도화지를 하나씩 BFS 탐색하며 그림의 개수와 가장 넓은 그림의 넓이를 출력한다.
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

count = 0
max_area = 0
for r in range(n):
    for c in range(m):
        if board[r][c]:
            board[r][c] = 0
            queue = deque([])
            queue.append([r, c])
            area = 1
            while queue:
                row, col = queue.popleft()
                for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    if 0<=row+dr<n and 0<=col+dc<m and board[row+dr][col+dc]:
                        board[row+dr][col+dc] = 0
                        queue.append([row+dr, col+dc])
                        area += 1
            count += 1
            max_area = max(max_area, area)

print(count, max_area, sep='\n')