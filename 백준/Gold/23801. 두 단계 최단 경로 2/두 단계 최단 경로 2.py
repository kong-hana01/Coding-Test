# https://www.acmicpc.net/problem/23801
# 접근 방법
# 도착지와 출발지에서 다익스트라 최단경로 알고리즘을 돌린 뒤, p 경로 중 distance가 가장 작은 것을 택해 이를 출력한다.
def dijkstra(start, distance):
    h = []
    heapq.heappush(h, (0, start))
    distance[start] = 0
    while h:
        dist, now = heapq.heappop(h)
        if distance[now] < dist:
            continue
        for next, cost in graph[now]:
            next_dist = dist + cost
            if distance[next] <= next_dist:
                continue
            distance[next] = next_dist
            heapq.heappush(h, (next_dist, next))

import sys, heapq
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
x, z = map(int, input().split())
p = int(input())
INF = int(1e13)
x_distance = [INF for _ in range(n+1)]
z_distance = [INF for _ in range(n+1)]
dijkstra(x, x_distance)
dijkstra(z, z_distance)
min_dist = INF
for y in list(map(int, input().split())):
    min_dist = min(min_dist, x_distance[y] + z_distance[y])
if min_dist == INF:
    print(-1)
else:
    print(min_dist)