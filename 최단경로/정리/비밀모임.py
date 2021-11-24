# https://www.acmicpc.net/problem/13424
# 접근 방법
# 친구가 있는 모든 위치에 대해 다익스트라 최단 경로 알고리즘을 돌리고, 그 거리의 합이 가장 작은 인덱스 번호를 출력한다.
def dijkstra(start):
    INF = int(1e9)
    distance = [INF for _ in range(n+1)]
    distance[start] = 0
    h = []
    heapq.heappush(h, [0, start])
    while h:
        dist, now = heapq.heappop(h)
        if distance[now] < dist:
            continue
        for x in graph[now]:
            cost = dist + x[1]
            if cost < distance[x[0]]:
                distance[x[0]] = cost
                heapq.heappush(h, [cost, x[0]])
    return distance

import sys, heapq
input = sys.stdin.readline
tc = int(input())
for _ in range(tc):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append([b, c])
        graph[b].append([a, c])
    k = int(input())
    friends = list(map(int, input().split()))
    total_distance = [0 for _ in range(n+1)]
    total_distance[0] = int(1e9)
    for s in friends:
        distance = dijkstra(s)
        for i in range(1, n+1):
            total_distance[i] += distance[i]
    print(total_distance.index(min(total_distance)))