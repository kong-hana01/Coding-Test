# https://www.acmicpc.net/problem/16724
# 접근 방법
# dfs를 통해 모든 위치를 탐색한 뒤, dfs의 탐색이 끝날 때마다 값을 하나씩 증가시켜주고 모든 탐색이 끝난 뒤, 값을 출력한다.
def get_parent(r, c):
    if parent[r][c] == (r, c):
        return (r, c)
    r1, c1 = parent[r][c]
    parent[r][c] = get_parent(r1, c1)
    return parent[r][c]

def find_union(r1, c1, r2, c2):
    x1 = get_parent(r1, c1)
    x2 = get_parent(r2, c2)
    if x1[0] < x2[0]:
        parent[r2][c2] = (r1, c1)
    elif x1[0] > x2[0]:
        parent[r1][c1] = (r2, c2)
    else:
        if x1[1] < x2[1]:
            parent[r2][c2] = (r1, c1)
        else:
            parent[r1][c1] = (r2, c2)

def dfs(r, c, row, col):
    if visited[r][c]:
        find_union(r, c, row, col)
        return 
    visited[r][c] = True
    parent[r][c] = (row, col)
    if graph[r][c] == 'D':
        dfs(r+1, c, row, col)
    elif graph[r][c] == "U":
        dfs(r-1, c,  row, col)
    elif graph[r][c] == "R":
        dfs(r, c+1, row, col)
    else:
        dfs(r, c-1, row, col)


import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
graph = [[x for x in input().rstrip()] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
parent = [[(i, j) for j in range(m)] for i in range(n)]
for r in range(n):
    for c in range(m):
        if not visited[r][c]:
            dfs(r, c, r, c)

count = 0
visited = [[False for _ in range(m)] for _ in range(n)]
for r in range(n):
    for c in range(m):
        r1, c1 = parent[r][c]
        r1, c1 = get_parent(r1, c1)
        parent[r][c] = (r1, c1)
        if not visited[r1][c1]:
            visited[r1][c1] = 1
            count += 1
print(count)
