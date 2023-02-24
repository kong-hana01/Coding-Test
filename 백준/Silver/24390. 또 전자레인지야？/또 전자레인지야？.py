# https://www.acmicpc.net/problem/24390
# 접근 방법
# bfs로 문제를 해결한다.
from collections import deque
queue = deque([])
m, s = map(int, input().split(":"))
s += m * 60
visited = [-1 for _ in range(3601)]
visited[0] = 1
visited[30] = 1
queue.append(0)
queue.append(30)
while queue:
    x = queue.popleft()
    for dx in [10, 60, 600]:
        if x+dx <= 3600 and visited[x+dx] == -1:
            visited[x+dx] = visited[x] + 1
            queue.append(x+dx)
print(visited[s])