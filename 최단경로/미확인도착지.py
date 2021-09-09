# https://www.acmicpc.net/problem/9370
# 접근 방법
# 각 테스트 케이스마다 다익스트라 최단경로 알고리즘을 진행한다.
# 단, 매 테스트 케이스를 시작할 때마다 목적지 후보의 지점을 오름차순으로 정렬한다. 그리고 다익스트라 최단경로 알고리즘을 진행할때마다 모든 지점에 대해 g와 h의 교차로를 지났는 지 체크해가며 알고리즘을 진행한다.
def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, [0, start])
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for x in graph[now]:
            cost = dist + x[1]
            if distance[x[0]] > cost:
                heapq.heappush(q, [cost, x[0]])
                distance[x[0]] = cost
                check[x[0]] = check[now]
                if (g == now and h == x[0]) or (h == now and g == x[0]):
                    check[x[0]] = 1

            elif distance[x[0]] == cost:
                check[x[0]] = max(check[x[0]], check[now])
                if (g == now and h == x[0]) or (h == now and g == x[0]):
                    check[x[0]] = 1
                    
import heapq, sys
input = sys.stdin.readline
for tc in range(int(input())):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append([b, d])
        graph[b].append([a, d])
    departure = []
    for _ in range(t):
        departure.append(int(input()))
    departure.sort()
    INF = int(1e9)
    distance = [INF for _ in range(n+1)]
    check = [0 for _ in range(n+1)]
    dijkstra(s)
    for x in departure:
        if check[x]:
            print(x, end=' ')
    print()