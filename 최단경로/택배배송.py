# https://www.acmicpc.net/problem/5972
# 접근 방법
# 다익스트라 최단경로 알고리즘을 활용해 문제를 해결한다.

def dijkstra(start):
    distance[start] = 0 
    q = []
    heapq.heappush(q, [0, start])
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for x in graph[now]:
            cost = dist + x[1]
            if distance[x[0]] > cost:
                heapq.heappush(q, [cost, x[0]])
                distance[x[0]] = cost

import sys, heapq
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
INF = int(1e9)
distance = [INF for _ in range(n+1)]
dijkstra(1)
print(distance[n])