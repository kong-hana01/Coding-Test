# https://www.acmicpc.net/problem/10217
# 접근 방법 -> 이후에 풀어보기
# 해당 문제의 시간 제한은 10초이다. 여러개의 테스트 케이스가 들어간다고 하더라도 넉넉한 시간 제한을 가지고 있다.
# 다익스트라 최단경로 알고리즘을 활용하는 것은 최단 경로를 갱신해가며 이미 방문한 위치는 방문하지 않는 것이 핵심이지만 가장 비용이 적은 것과 소요시간이 적은 것을 따로 구분하여 할 수 없다.
# 따라서 두 가지 요소를 점검한 뒤, 더 적은 소요시간으로 탐색하거나, 비용이 적은 경우 각 노드에 대해 비용과 시간을 갱신하고, 우선순위 큐로 탐색한다.

def dijkstra(start):
    cost[start] = 0
    time[start] = 0
    q = []
    heapq.heappush(q, [0, 0, start]) # cost, time, node
    while q:
        c, d, now = heapq.heappop(q)
        if cost[now] < c and time[now] < d:
            continue
        for x in graph[now]:
            c_ = c + x[1]
            d_ = d + x[2]
            if c_ < m and (c_ < cost[x[0]] or d_ < time[x[0]]):
                heapq.heappush(q, [c_, d_, x[0]])
                # cost

import heapq, sys
input = sys.stdin.readline

for tc in range(int(input())):
    n, m, k = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(k):
        u, v, c, d = map(int, input().split())
        graph[u].append([v, c, d])
    INF = int(1e9)
    cost = [INF for _ in range(n+1)]
    time = [INF for _ in range(n+1)]