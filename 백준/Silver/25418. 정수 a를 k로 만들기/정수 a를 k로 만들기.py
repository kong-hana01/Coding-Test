# https://www.acmicpc.net/problem/25418
# 접근 방법
# bfs를 사용해 문제를 해결한다.
from collections import deque
a, k = map(int, input().split())
visited = [-1 for _ in range(k+1)]
queue = deque([])
queue.append(a)
visited[a] = 0
while queue:
    x = queue.popleft()
    if x+1 <= k and visited[x+1] == -1:
        visited[x+1] = visited[x] + 1
        queue.append(x+1)
    if x*2 <= k and visited[x*2] == -1:
        visited[x*2] = visited[x] + 1
        queue.append(x*2)
print(visited[k])