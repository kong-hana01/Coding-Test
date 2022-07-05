# https://www.acmicpc.net/problem/22865
# 접근 방법
# a, b, c에서 다익스트라를 사용해 가장 먼 곳을 구한 뒤, 가장 먼 곳의 땅 번호를 출력한다.
def dijkstra(start):
    distance[start] = 0
    h = []
    heapq.heappush(h, [0, start])
    while h:
        dist, now = heapq.heappop(h)
        if dist > distance[now]:
            continue
        for x in graph[now]:
            cost = dist + x[1] 
            if cost < distance[x[0]]:
                distance[x[0]] = cost
                heapq.heappush(h, [cost, x[0]])

import sys, heapq
input = sys.stdin.readline
n = int(input())
a, b, c = map(int ,input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    d, e, l = map(int ,input().split())
    graph[d].append([e, l])
    graph[e].append([d, l])

INF = 1e10
totalDist = [INF for _ in range(n+1)] # total, min
for i, x in enumerate([a, b, c]):
    distance = [INF for _ in range(n+1)]
    dijkstra(x)
    for j in range(1, n+1):
        totalDist[j] = min(totalDist[j], distance[j])
result = 1
for i in range(2, n+1):
    if totalDist[result] < totalDist[i]:
        result = i
print(result)