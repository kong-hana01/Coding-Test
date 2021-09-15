# https://www.acmicpc.net/problem/1719
# 접근 방법
# 각 집하장에서 다른 집하장으로 가는 다익스트라 최단경로를 갱신해가며 1번부터 n번까지의 각각 최단 경로를 출력한다.
def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, [0, start, start])

    while q:
        dist, now, pre = heapq.heappop(q)
        if distance[now] < dist:
            continue
        if move[now] == now and start != pre:
            move[now] = pre

        if now == pre or pre == start:
            next = now
        else:
            next = pre

        for x in graph[now]:
            cost = dist + x[1]
            if distance[x[0]] > cost:
                distance[x[0]] = cost
                heapq.heappush(q, [cost, x[0], next])

import heapq
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
INF = int(1e9)
for _ in range(m):
    u, v, c = map(int, input().split())
    graph[u].append([v, c])
    graph[v].append([u, c])

for i in range(1, n+1):
    distance = [INF for _ in range(n+1)]
    move = [i for i in range(n+1)]
    dijkstra(i)
    for j in range(1, n+1):
        if i == j:
            print('-', end = ' ')
        else:
            print(move[j], end = ' ')
    print()