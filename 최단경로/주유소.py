# https://www.acmicpc.net/problem/13308
# 접근 방법 2 
# 다익스트라 최단 경로 알고리즘을 활용하는 대신 최소 힙에 최소 리터당 기름 값을 갱신해가며 이를 기준으로 값을 갱신한다.
# 또한 각 지역에 방문처리를 하기 위해 nxn 배열을 만들어 거리를 갱신한다.
def dijkstra(start):
    q = []
    heapq.heappush(q, [0, start, start, cost[start]]) # 현재까지의 비용, 현재위치, 이전위치, 리터당 최소값
    while q:
        total_cost, now_city, last_city, liter_per_min_cost = heapq.heappop(q)
        if now_city == n:
            return
        #if total_cost > distance[last_city][now_city]:
        #    continue
        for x in graph[now_city]:
            next_cost = total_cost + x[1] * liter_per_min_cost
            # if next_cost < distance[now_city][x[0]]:
            heapq.heappush(q, [next_cost, x[0], now_city, min(liter_per_min_cost, cost[x[0]])])
            distance[now_city][x[0]] = min(next_cost, distance[now_city][x[0]])

import heapq
n, m = map(int, input().split())
cost = [0] + list(map(int, input().split()))
graph = [[] for _  in range(n+1)]
for _ in range(m):
    a, b, l = map(int, input().split())
    graph[a].append([b, l])
    graph[b].append([a, l])
INF = int(1e11)
distance = [[INF for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    distance[i][i] = 0

dijkstra(1)
min_value = INF
for x in distance[:n]:
    min_value = min(x[-1], min_value)
print(min_value)

# 접근 방법 1 -> 시간 부족으로 인해 다음에 해결
# 다익스트라 최단 경로 알고리즘을 활용한다. 단, 거리 갱신의 기준은 현재 노드에서 다른 노드로 이동하기 위한 비용을 기준으로 한다.
# def dijkstra(start):
#     distance[start] = 0
#     q = []
#     heapq.heappush(q, [0, start, city[start]])

#     while q:
#         now_cost, now_city, min_cost = heapq.heappop(q)
#         if distance[now_city] < now_cost:
#             continue
#         min_cost = min(city[now_city], min_cost)
#         for x in graph[now_city]:
#             cost = x[1] * min_cost + now_cost
#             if distance[x[0]] > cost:
#                 distance[x[0]] = cost
#                 heapq.heappush(q, [cost, x[0], min_cost])
    

# import heapq
# n, m = map(int, input().split())
# city = [0] + list(map(int, input().split()))
# graph = [[] for _ in range(n+1)]
# for _ in range(m):
#     a, b, dist = map(int, input().split())
#     graph[a].append([b, dist])
#     graph[b].append([a, dist])
# INF = int(1e9)
# distance = [INF for _ in range(n+1)]
# dijkstra(1)
# print(distance)