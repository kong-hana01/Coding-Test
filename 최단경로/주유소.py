# https://www.acmicpc.net/problem/13308
# 접근 방법 1 -> 시간 부족으로 인해 다음에 해결
# 다익스트라 최단 경로 알고리즘을 활용한다. 단, 거리 갱신의 기준은 현재 노드에서 다른 노드로 이동하기 위한 비용을 기준으로 한다.
def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, [0, start, city[start]])

    while q:
        now_cost, now_city, min_cost = heapq.heappop(q)
        if distance[now_city] < now_cost:
            continue
        min_cost = min(city[now_city], min_cost)
        for x in graph[now_city]:
            cost = x[1] * min_cost + now_cost
            if distance[x[0]] > cost:
                distance[x[0]] = cost
                heapq.heappush(q, [cost, x[0], min_cost])
    

import heapq
n, m = map(int, input().split())
city = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, dist = map(int, input().split())
    graph[a].append([b, dist])
    graph[b].append([a, dist])
INF = int(1e9)
distance = [INF for _ in range(n+1)]
dijkstra(1)
print(distance)