# https://www.acmicpc.net/problem/18352
# 접근 방법
# 다익스트라 최단경로를 활용해 최단 거리가 k인 도시의 번호를 오름차순으로 출력한다.
def dijkstra(start):
    h = []
    heapq.heappush(h, [0, start])
    distance[start] = 0
    while h:
        dist, now = heapq.heappop(h)    
        if distance[now] < dist:
            continue
        for next in graph[now]:
            if distance[next] > dist + 1:
                heapq.heappush(h, [dist + 1, next])
                distance[next] = dist + 1


import heapq, sys
input = sys.stdin.readline
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
INF = int(1e9)
distance = [INF for _ in range(n+1)]
dijkstra(x)
result = []
for i in range(1, n+1):
    if distance[i] == k:
        result.append(i)
if result:
    for x in result:
        print(x)
else:
    print(-1)