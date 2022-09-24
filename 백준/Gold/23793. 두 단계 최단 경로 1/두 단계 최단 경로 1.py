# https://www.acmicpc.net/problem/23793
# 접근 방법
# y를 거치는 방법과 y를 거치지 않는 방법을 모두 distance에 구현해 이를 해결한다.
def dijkstra(start, y):
    distance[0][start] = 0
    h = []
    heapq.heappush(h, [0, 0, start]) # dist, visited, start
    while h:
        dist, visited, now = heapq.heappop(h)
        if distance[visited][now] < dist:
            continue
        for next, add_dist in graph[now]:
            next_visited = 1 if visited or (not visited and next == y) else 0
            if distance[next_visited][next] > dist + add_dist:
                distance[next_visited][next] = dist + add_dist
                heapq.heappush(h, [dist+add_dist, next_visited, next]) 


import sys, heapq
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

x, y, z = map(int, input().split())
INF = int(1e10)
distance =[[INF for _ in range(n+1)] for _ in range(2)]
dijkstra(x, y)
print(distance[1][z] if distance[1][z] != INF else -1, distance[0][z] if distance[0][z] != INF else -1)