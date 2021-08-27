# https://www.acmicpc.net/problem/1939
# 접근 방법 1
# 다익스트라 최단 경로 알고리즘을 활용해 중량을 합산하지 않고, 최댓값을 기준으로 경로를 초기화한다.
def dijkstra(start):
    q = []
    heapq.heappush(q, [-int(1e9), start])

    while q:
        w, now = heapq.heappop(q)
        if weight[now] >= -w:
            continue
        for x in graph[now]:
            if weight[x[0]] < min(x[1], -w) or not weight[x[0]]:
                heapq.heappush(q, [-x[1], x[0]])
                weight[x[0]] = min(x[1], -w)

import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
weight = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

target = list(map(int, input().split()))
dijkstra(target[0])
print(weight[target[1]])