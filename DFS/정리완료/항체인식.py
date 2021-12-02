# https://www.acmicpc.net/problem/22352
# 접근 방법
# 이전 촬영 결과과 이후 촬영 결과가 다른 지점을 dfs 탐색한 뒤, 모든 값을 확인한다.

def dfs(r, c, v):
    visited[r][c] = True
    last_v = last[r][c]
    last[r][c] = v
    for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        if 0<=r+dr<=n-1 and 0<=c+dc<=m-1 and last[r+dr][c+dc] == last_v and not visited[r+dr][c+dc]:
            dfs(r+dr, c+dc, v)

n, m = map(int, input().split())
last = [list(map(int, input().split())) for _ in range(n)]
post = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

check = True
for r in range(n):
    for c in range(m):
        if last[r][c] != post[r][c]:
            dfs(r, c, post[r][c])
            check = False
            break
    if not check:
        break
check = True
for r in range(n):
    for c in range(m):
        if last[r][c] != post[r][c]:
            check = False
            break

if check:
    print('YES')
else:
    print("NO")