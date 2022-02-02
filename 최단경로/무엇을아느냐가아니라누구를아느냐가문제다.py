# https://www.acmicpc.net/problem/9694
# 접근 방법
# 다익스트라 알고리즘을 활용해 친밀도의 합이 가장 작은 값을 출력한다.
def dijkstra(s):
    dist[s] = 0
    h = []
    heapq.heappush(h, [0, s])
    path[s] = [s]
    while h:
        d, now = heapq.heappop(h)
        if dist[now] < d:
            continue
        for x in graph[now]:
            cost = x[1] + d
            if cost < dist[x[0]]:
                path[x[0]] = path[now] + [x[0]]
                dist[x[0]] = cost
                heapq.heappush(h, [cost, x[0]])

import heapq
tc = int(input())
for i in range(1, tc + 1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(m)]
    path = [[] for _ in range(m)]
    for _ in range(n):
        x, y, z = map(int, input().split())
        graph[x].append([y, z])
        graph[y].append([x, z])
        
    INF = int(1e4)
    dist = [INF for _ in range(m)]
    dijkstra(0)
    print(f'Case #{i}:', end=' ')
    if path[-1]:
        for x in path[-1]:
            print(x, end=' ')
    else:
        print(-1)
    print()