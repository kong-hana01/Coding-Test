# https://www.acmicpc.net/problem/20168
# 접근방법
# 다익스트라 최단경로 알고리즘을 통해 골목 요금의 최댓값의 최솟값을 구한다.
def dijkstra(start):
    global result
    h = []
    heapq.heappush(h, [0, 0, start])
    while h:
        max_cost, total_cost, now = heapq.heappop(h)
        if total_cost > c:
            continue
        for x in graph[now]:
            cost = total_cost + x[1]
            if cost > c or visited[now][x[0]]:
                continue
            elif x[0] == end:
                result = min(result, max(max_cost, x[1]))
            visited[now][x[0]] = True
            heapq.heappush(h, [max(max_cost, x[1]), cost, x[0]])


import heapq
n, m, start, end, c = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [[False for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])
    graph[b].append([a, cost])
INF = int(1e9)
result = INF
dijkstra(start)
if result != INF:
    print(result)
else:
    print(-1)