# https://www.acmicpc.net/problem/1103
# 접근 방법
# DFS를 사용해 문제를 해결한다. 
# 최대 단위 연산 횟수: (50 x 50)
# def dfs(r, c, visited):
#     global is_loop
#     if is_loop:
#         return
#     global result
#     result = max(result, len(visited))
#     step = int(board[r][c])
#     for dr, dc in [[step, 0], [-step, 0], [0, step], [0, -step]]:
#         if 0<=r+dr<n and 0<=c+dc<m and board[r+dr][c+dc] != "H":
#             if (r + dr) * m + c + dc in visited:
#                 is_loop = True
#                 return 
#             next = ((r + dr) * m + c + dc)
#             dfs(r+dr, c+dc, visited|{next})
    
# def run():
#     global is_loop
#     for r in range(n):
#         for c in range(m):
#             if board[r][c] != 'H':
#                 dfs(r, c, {r*m+c})
#             if is_loop:
#                 return

def dfs(r, c, visited):
    if dp[r][c]:
        return dp[r][c]
    
    step = int(board[r][c])
    for dr, dc in [[step, 0], [-step, 0], [0, step], [0, -step]]:
        if 0<=r+dr<n and 0<=c+dc<m and board[r+dr][c+dc] != "H":
            if (r + dr) * m + c + dc in visited:
                dp[r+dr][c+dc] = -1
                return dp[r+dr][c+dc]
            next = ((r + dr) * m + c + dc)
            cnt = dfs(r+dr, c+dc, visited|{next})
            if cnt == -1:
                return cnt
            dp[r][c] = max(dp[r][c], cnt + 1)
    
    return dp[r][c]

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int, input().split())
board = [[x for x in input()] for _ in range(n)]
result = 0
is_loop = False
# run()
dp = [[0 for _ in range(m)] for _ in range(n)]
dfs(0, 0, {0})
if min(map(lambda x: min(x), dp)) == -1:
    print(-1)
else:
    print(max(map(lambda x: max(x), dp)) + 1)