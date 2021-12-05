# https://www.acmicpc.net/problem/1504
# 접근 방법
# 다익스트라 최단 경로 문제의 응용 문제이다.
# 임의로 주어진 두 정점과의 거리를 계산하고, 각 정점에서 N번 정점까지 가는 최단 경로를 구한 뒤, 각각을 더해 최단 경로의 비용을 계산한다.

def dijkstra(start, distance):
    distance[start] = 0
    q = []
    heapq.heappush(q, [0, start])
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for x in graph[now]:
            cost = dist + x[1]
            if cost < distance[x[0]]:
                distance[x[0]] = cost
                heapq.heappush(q, [cost, x[0]])
        
import sys, heapq
input = sys.stdin.readline
n, e = map(int, input().split())
INF = int(1e9)
distance = [INF for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c]) # 양방향 길이 존재

v1, v2 = map(int, input().split())
dijkstra(1, distance)
dist1 = [INF for _ in range(n+1)]
dist2 = [INF for _ in range(n+1)]
dijkstra(v1, dist1)
dijkstra(v2, dist2)
result = min(distance[v1] + dist1[v2] + dist2[n], distance[v2] + dist2[v1] + dist1[n])
if result >= INF:
    result = -1
print(result)