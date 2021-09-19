# 접근 방법
# 모든 지역을 한번씩 다익스트라 최단경로 알고리즘을 활용해 탐색한 뒤 가장 많은 물건을 얻는 경우의 물건 개수를 출력한다.
# 단 다익스트라를 사용할 때 예은이가 이동할 수 있는 거리보다 작거나 같은 경우만 이를 저장한다.
def dijkstra(start):
    global result
    INF = int(1e9)
    q = []
    heapq.heappush(q, [0, start])
    distance[start] = 0
    count = items[start]
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for x in graph[now]:
            cost = x[1] + dist
            if distance[x[0]] > cost and cost <= m:
                heapq.heappush(q, [cost, x[0]])
                if distance[x[0]] == INF:
                    count += items[x[0]]
                distance[x[0]] = cost
    result = max(result, count)
            
import sys, heapq
input = sys.stdin.readline

n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append([b, l])
    graph[b].append([a, l])

INF = int(1e9)
result = 0
for i in range(1, n+1):
    distance = [INF for _ in range(n+1)]
    dijkstra(i)
print(result)