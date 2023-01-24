# https://www.acmicpc.net/problem/18111
# 접근 방법
# 높이를 최소 높이뷰터 최대 높이까지 하나씩 대입하여 브루트포스를 해본다.
import sys
input = sys.stdin.readline
n, m, b = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
min_height, max_height = board[0][0], board[0][0]
for r in range(n):
    for c in range(m):
        min_height = min(min_height, board[r][c])
        max_height = max(max_height, board[r][c])

result = [256*n*m, 0]
for height in range(min_height, max_height+1):
    now_block = b
    elaps_time = 0
    for r in range(n):
        for c in range(m):
            if board[r][c] >= height:
                diff = board[r][c] - height
                now_block += diff
                elaps_time += diff * 2
            else:
                diff = height - board[r][c]
                elaps_time += diff
                now_block -= diff
    if now_block < 0:
        continue
    if elaps_time <= result[0]:
        result = [elaps_time, height]
print(*result)