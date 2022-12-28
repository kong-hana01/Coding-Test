# https://www.acmicpc.net/problem/2458
# 접근 방법
# BFS를 사용해 한 노드에서 다른 모든 노드로 갈 수 있다면 본인의 순위를 알 수 있기에 이를 카운트해 출력한다.
from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


for i in range(1, n+1):
    queue = deque([])
    queue.append(i)
    visited[i][i] = 1
    while queue:
        x = queue.popleft()
        for next in graph[x]:
            if not visited[i][next]:
                visited[i][next] = 1
                visited[next][i] = 1
                queue.append(next)

count = 0    
for i in range(1, n+1):
    if sum(visited[i][1:]) == n:
        count += 1

print(count)