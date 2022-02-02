# https://www.acmicpc.net/problem/11779
# 접근 방법
# 다익스트라 알고리즘을 활용해 문제를 해결한다.
def dijkstra(start, end, distance, graph):
    distance[start] = 0
    q = []
    heapq.heappush(q, [0, start])
    city[start] = [start]
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for x in graph[now]:
            cost = dist + x[1]
            if distance[x[0]] > cost:
                heapq.heappush(q, [cost, x[0]])
                distance[x[0]] = cost
                city[x[0]] = city[now] + [x[0]]
    

import heapq, sys
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
start, end = map(int, input().split())
INF = int(1e9)
distance = [INF for _ in range(n+1)]
city = [[] for _ in range(n+1)]
dijkstra(start, end, distance, graph)
print(distance[end])
print(len(city[end]))
for i in range(len(city[end])):
    print(city[end][i], end=' ')