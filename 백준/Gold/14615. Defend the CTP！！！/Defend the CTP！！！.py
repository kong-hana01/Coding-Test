# https://www.acmicpc.net/problem/14615
# 접근 방법
# 1번 도시에서 다른 도시까지 갈 수 있는지 여부를 체크한다.
# 다른 도시들에서 N번 도시까지 갈 수 있는지 여부를 매 시나리오마다 누적하여 체크한다.
# 위의 두 정보를 활용해 문제를 해결한다.
def bfs(now, graph, visited):
    queue = deque([])
    queue.append(now)
    while queue:
        now = queue.popleft()
        for next in graph[now]:
            if visited[next]:
                continue
            queue.append(next)
            visited[next] = True

from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph1 = [[] for _ in range(n+1)]
graph2 = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph1[x].append(y)
    graph2[y].append(x)
visited1 = [0 for _ in range(n+1)]
visited2 = [0 for _ in range(n+1)]
bfs(1, graph1, visited1)
bfs(n, graph2, visited2)

t = int(input())
for _ in range(t):
    x = int(input())
    if visited1[x] and visited2[x]:
        print('Defend the CTP')
    else:
        print('Destroyed the CTP')