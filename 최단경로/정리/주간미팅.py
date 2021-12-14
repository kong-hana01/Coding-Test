# https://www.acmicpc.net/problem/12834
# 접근 방법
# 1. KIST의 위치와 씨알푸드의 위치로부터 다른 장소의 위치까지의 거리를 다익스트라 최단경로 알고리즘을 활용해 구한다.(위의 간선은 양방향임)
# 2. 각 위치는 KIST와 씨알푸드의 거리 값을 기준으로 이중리스트로 구성하여 이를 처리한다.
def dijkstra(start, idx):
    distance[start][idx] = 0
    h = []
    heapq.heappush(h, [0, start])
    while h:
        dist, now = heapq.heappop(h)
        if distance[now][idx] < dist:
            continue
        for x in graph[now]:
            cost = x[1] + dist
            if distance[x[0]][idx] > cost:
                distance[x[0]][idx] = cost
                heapq.heappush(h, [cost, x[0]])


import sys, heapq
input = sys.stdin.readline
n, v, e = map(int, input().split())
A, B = map(int, input().split())
h = list(map(int, input().split()))
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, l = map(int, input().split())
    graph[a].append([b, l])
    graph[b].append([a, l])
INF = int(1e8)
distance = [[INF, INF] for _ in range(v+1)]
dijkstra(A, 0)
dijkstra(B, 1)
result = 0
for i in h:
    if distance[i][0] == INF:
        distance[i][0] = -1
    if distance[i][1] == INF:
        distance[i][1] = -1
    result += distance[i][0] + distance[i][1]
print(result)