# # https://www.acmicpc.net/problem/15559
# # 접근 방법 1
# # 분리집합을 사용하여 각 위치별로 다음 위치를 체크한 뒤, 분리집합의 개수를 체크해 이를 출력한다.
def calc_dxdy(r, c):
    if board[r][c] == 'N':
        return -1, 0
    elif board[r][c] == 'S':
        return 1, 0
    elif board[r][c] == 'W':
        return 0, -1
    else:
        return 0, 1

def dfs(r, c):
    if visited[r][c]:
        if union[r][c]:
            return union[r][c] 
        else:
            global union_num
            union_num += 1
            union[r][c] = union_num
            return union[r][c]

    visited[r][c] = True
    dx, dy = calc_dxdy(r, c)
    union[r][c] = dfs(r+dx, c+dy)
    return union[r][c]

import sys
sys.stdin.readline
sys.setrecursionlimit(10**7)
n, m = map(int, input().split())
board = [[x for x in input()] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
union = [[0 for _ in range(m)] for _ in range(n)]
union_num = 0
for r in range(n):
    for c in range(m):
        dfs(r, c)
print(union_num)