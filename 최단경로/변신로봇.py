# https://www.acmicpc.net/problem/14630
# 접근 방법
# 다익스트라 최단경로 알고리즘을 활용해 원하는 변신 상태로 만드는 데에 필요한 돈의 최솟값을 출력한다.
def dijkstra(start):
    distance[start] = 0
    h = []
    heapq.heappush(h, [0, start])
    while h:
        dist, now = heapq.heappop(h)
        if distance[now] < dist:
            continue
        for i in range(1, n+1):
            if i == now:
                continue
            cost = dist
            for j in range(len(parts[i])):
                cost += (parts[i][j] - parts[now][j]) ** 2
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(h, [cost, i])

import heapq
n = int(input())
parts = [[]] + [[int(x) for x in input()] for _ in range(n)]
start, end = map(int, input().split())
INF = int(1e9)
distance = [INF for _ in range(n+1)]
dijkstra(start)
print(distance[end])