# https://www.acmicpc.net/problem/13565
# 접근 방법
# DFS 탐색을 통해 첫번째 행에서 출발해 마지막 행에 도착하는지 판단한다.
# 만일 도착한다면 YES, 끝까지 도착하지 못한다면 NO를 출력한다.
import sys
sys.setrecursionlimit(10**6)
def dfs(r, c):
    if r == m-1:
        return True
    for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        if 0<=r+dr<m and 0<=c+dc<n and not board[r+dr][c+dc]:
            board[r+dr][c+dc] = 1
            if dfs(r+dr, c+dc):
                return True
    return False

input = sys.stdin.readline
m, n = map(int, input().split())
board = [[int(x) for x in input().rstrip()] for _ in range(m)]
flag = False
for c in range(n):
    if not board[0][c]:
        board[0][c] = 1
        if dfs(0, c):
            flag = True
            break
if flag:
    print('YES')
else:
    print("NO")
