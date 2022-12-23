# https://www.acmicpc.net/problem/2982
# 접근 방법
# 고둘라부터 이동한 뒤, 그 시간에 맞게 주어진 조건에 대해 다익스트라 최단 경로 알고리즘을 돌린다.
def dijkstra(start, k):
    h = []
    heapq.heappush(h, [k, start])
    distance[start] = k
    while h:
        dist, now = heapq.heappop(h)
        if distance[now] < dist:
            continue
        for next, cost, idx in graph[now]:
            if intersections[idx][3] == -1 or intersections[idx][3] > dist or intersections[idx][3] + intersections[idx][2] <= dist:
                next_cost = dist + cost
            else:
                next_cost = intersections[idx][3] + intersections[idx][2] + cost
            if distance[next] > next_cost:
                distance[next] = next_cost
                heapq.heappush(h, [next_cost, next])

import sys, heapq
input = sys.stdin.readline
n, m = map(int, input().split())
a, b, k, g = map(int, input().split())
g_path = list(map(int, input().split()))
g_distance = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
INF = int(1e7)
distance = [INF for _ in range(n+1)]
intersections = [[]]
for i in range(1, m+1):
    u, v, l = map(int, input().split())
    graph[u].append([v, l, i])
    graph[v].append([u, l, i])
    intersections.append([u, v, l, -1])


now = 0
for i in range(g-1):
    p = g_path[i]
    for next, cost, j in graph[p]:
        if g_path[i+1] == next:            
            intersections[j][3] = now
            now += intersections[j][2]
            break

dijkstra(a, k)
print(distance[b] - distance[a])