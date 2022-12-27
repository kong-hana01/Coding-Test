# https://www.acmicpc.net/problem/11952
# 접근 방법
# 초기에 k개의 도시를 모두 bfs에 넣고 각 도시별로 어떤 도시가 위험한지 체크한다.
# 이후 1번 도시부터 n번 도시까지 이동할 때의 최단 경로를 계산한다.
def dijkstra(s):
    h = []
    heapq.heappush(h, [0, s])
    distance[s] = 0
    while h:
        dist, now = heapq.heappop(h)
        if distance[now] < dist:
            continue
        for next in graph[now]:
            if danger[next] == 0:
                continue
            if danger[next] == -1:
                cost = dist + p
            else:
                cost = dist + q
            if distance[next] > cost:
                distance[next] = cost
                heapq.heappush(h, [cost, next])

import sys, heapq
from collections import deque
sys.stdin.readline
n, m, k, s = map(int, input().split())
p, q = map(int, input().split())
queue = deque([])
danger = [-1 for _ in range(n+1)]
INF = int(1e11)
distance = [INF for _ in range(n+1)]
for _ in range(k):
    city = int(input())
    queue.append(city)
    danger[city] = 0

graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

while queue:
    x = queue.popleft()
    for next in graph[x]:
        if danger[next] == -1 and danger[x] < s:
            danger[next] = danger[x] + 1
            queue.append(next)

dijkstra(1)
print(distance[n] - p if danger[n] == -1 else distance[n] - q)