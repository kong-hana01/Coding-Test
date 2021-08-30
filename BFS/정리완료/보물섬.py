# https://www.acmicpc.net/problem/2589
# 접근 방법
# 모든 w에 대해 bfs를 탐색한 뒤, 가장 값이 높게 나온 것을 출력한다.
# 최대 연산 횟수: 50 x 50 x 2500 x 2 = 13,000,000회

def bfs(r, c):
    global time
    board = [x[:] for x in map_]
    queue = deque([])
    queue.append([r, c])
    board[r][c] = 0

    while queue:
        r_, c_ = queue.popleft()
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if 0<=r_+dr<=row-1 and 0<=c_+dc<=col-1 and board[r_+dr][c_+dc] == 'L':
                board[r_+dr][c_+dc] = board[r_][c_] + 1
                queue.append([r_+dr, c_+dc])
        time = max(time, board[r_][c_])

from collections import deque
import sys
input = sys.stdin.readline
row, col = map(int, input().split())
map_ = [[x for x in input().rstrip()] for _ in range(row)]
time = 0

for r in range(row):
    for c in range(col):
        if map_[r][c] == 'L':
            bfs(r, c)
print(time)