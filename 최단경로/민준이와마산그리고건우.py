# https://www.acmicpc.net/problem/18223
# 접근 방법
# 다익스트라 최단경로 알고리즘을 통해 최단 경로를 구한다.
# 단 최단경로를 갱신할 때는 이전 노드의 값을 추가로 갱신한다.
# 모든 탐색이 끝난 뒤, V정점에서 DFS를 통해 건우가 있는 지 확인하여 있으면 SAVE HIM, 없다면 GOOD BYE를 출력한다.
def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, [0, start])
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for x in graph[now]:
            cost = x[1] + dist
            if distance[x[0]] > cost:
                distance[x[0]] = cost
                parent[x[0]] = [now]
                heapq.heappush(q, [cost, x[0]])
            elif distance[x[0]] == cost:
                parent[x[0]].append(now)
                heapq.heappush(q, [cost, x[0]])

def find_friend(idx):
    if idx == p:
        return True
    for i in parent[idx]:
        if find_friend(i):
            return True

    return False

import heapq, sys
sys.setrecursionlimit(10**6)
v, e, p = map(int, input().split())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
INF = int(1e9)
distance = [INF for _ in range(v+1)]
parent = [[] for i in range(v+1)]
dijkstra(1)
if find_friend(v):
    print('SAVE HIM')
else:
    print('GOOD BYE')
