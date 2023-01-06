def dijkstra(start, limit):
    h = []
    heapq.heappush(h, [0, start])
    distance[start] = 0
    while h:
        now_cost, now = heapq.heappop(h)
        if distance[now] < now_cost:
            continue
        for next, cost in graph[now]:
            next_cost = now_cost + cost
            if next_cost <= c < distance[next] and cost <= limit:
                distance[next] = next_cost
                heapq.heappush(h, [next_cost, next])

import heapq, sys
input = sys.stdin.readline

n, m, start, end, c = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])
    graph[b].append([a, cost])

INF = int(1e12)
is_success = False
cnt = 0
while not is_success and cnt <= 20:
    cnt += 1
    distance = [INF for _ in range(n+1)]
    dijkstra(start, cnt)
    if distance[end] != INF:
        is_success = True
        continue
        
if cnt == 21:
    print(-1)
else:
    print(cnt)