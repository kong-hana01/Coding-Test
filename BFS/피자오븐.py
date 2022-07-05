# https://www.acmicpc.net/problem/19940
# 접근 방법
# BFS를 통해 문제를 해결한다.
from collections import deque
tc = int(input())
n_arr = [int(input()) for _ in range(tc)]
maxN = max(n_arr) + 10
visited = [[] for _ in range(maxN)]
visited[0] = [0, 0, 0, 0, 0]
queue = deque([])
queue.append(0)
for n in n_arr:
    while not visited[n]:
        x = queue.popleft()
        for i, dx in enumerate([60, 10, -10, 1, -1]):
            if 0<=x+dx<maxN and not visited[x+dx]:
                visited[x+dx] = visited[x][:]
                visited[x+dx][i] += 1
                queue.append(x+dx)
        print(queue)
    print(*visited[n])