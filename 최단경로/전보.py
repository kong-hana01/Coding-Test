import sys, heapq
input = sys.stdin.readline

n, m, c = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
INF = int(1e9)
distance = [INF for _ in range(n+1)]

# 각 노드에 대한 간선 정보 입력
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append([y, z])

def dijkstra(start):
    
    distance[start] = 0
    h = []
    heapq.heappush(h, [distance[start], start])
    while h:
        dis, node = heapq.heappop(h)
        if dis > distance[node]:
            continue
        visited[node] = True
        for data in graph[node]:        
            if not visited[data[0]] and data[1]+dis < distance[data[0]]:
                distance[data[0]] = data[1]+dis
                heapq.heappush(h, [distance[data[0]], data[0]])

dijkstra(c)

count = 0
max_distance = 0
for i in range(n):
    if distance[i] != INF:
        count += 1
        max_distance = max(max_distance, distance[i])
print(count, max_distance)