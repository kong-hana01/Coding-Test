# https://www.acmicpc.net/problem/2211
# 접근 방법
# 1번 컴퓨터에서 다익스트라 최단경로 알고리즘을 활용해 이전에 이동한 장소를 heap에 따로 저장하여 해당 위치에 대해서 탐색할 때마다 해당 값으로 갱신한다.
def dijkstra(s):
    distance[s] = 0
    h = []
    heapq.heappush(h, [0, 0, 1]) # dist, post, now
    result = []
    while h:
        dist, post, now = heapq.heappop(h)
        if dist > distance[now]:
            continue
        result.append([post, now])
        for x in graph[now]:
            cost = x[1] + dist
            if cost < distance[x[0]]:
                distance[x[0]] = cost
                heapq.heappush(h, [cost, now, x[0]])
    return result

import heapq, sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
INF = int(1e7)
distance = [INF for _ in range(n+1)]
result = dijkstra(1)
print(len(result) - 1)
for List in result[1:]:
    print(List[0], List[1])