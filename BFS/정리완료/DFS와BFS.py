import sys
from collections import deque
n, m, v = map(int, sys.stdin.readline().split())
line = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
map_ = [[] for _ in range(n+1)]

# 인덱스를 기준으로 한 map 만들기
for x1, x2 in line:
    map_[x1].append(x2)
    map_[x2].append(x1)

visited = [False] * n
dfs_ = []
def dfs(v):
    visited[v-1] = True
    dfs_.append(str(v))
    for x in sorted(map_[v]):
        if not visited[x-1]:
            dfs(x)

dfs(v)

visited = [False] * n
bfs_ = []
def bfs(v):
    visited[v-1] = True
    queue = deque([v])
    while queue:
        q = queue.popleft()
        bfs_.append(str(q))
        for x in sorted(map_[q]):
            if not visited[x-1]:
                queue.append(x)
                visited[x-1] = True

bfs(v)
print(" ".join(dfs_))
print(" ".join(bfs_))
