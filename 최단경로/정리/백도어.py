# https://www.acmicpc.net/problem/17396
# 접근 방법
# 다익스트라 최단 경로 알고리즘을 활용해 해당 문제를 해결한다.
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
            if distance[x[0]] > cost and not eyesight[x[0]]:
                distance[x[0]] = cost
                heapq.heappush(q, [cost, x[0]])
            elif x[0] == n-1:
                distance[x[0]] = min(cost, distance[x[0]])


import sys, heapq
input = sys.stdin.readline
n, m = map(int, input().split())
eyesight = list(map(int, input().split()))
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append([b, t])
    graph[b].append([a, t])
INF = int(1e11)
distance = [INF for _ in range(n)]
dijkstra(0)
if distance[-1] == INF:
    print(-1)
else:   
    print(distance[-1])