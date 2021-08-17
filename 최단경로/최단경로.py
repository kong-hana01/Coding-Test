import heapq, sys

def dijkstra(k):
    
    distance[k] = 0
    h = []
    heapq.heappush(h, [distance[k], k])

    while h:
        dist, node = heapq.heappop(h)
        if dist > distance[node]:
            continue
        for node_, dist_ in graph[node]:
            if dist_ + distance[node] >= distance[node_]:
                continue
            heapq.heappush(h, [dist_+distance[node], node_])
            distance[node_] = dist_+distance[node]

input = sys.stdin.readline
v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
INF = int(1e9)
distance = [INF for _ in range(v+1)]
k = int(input())
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append([v, w]) # [도착노드, 가중치]
    
dijkstra(k)
for x in distance[1:]:
    if x == INF:
        print('INF')
    else:
        print(x)