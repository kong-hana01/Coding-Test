# https://www.acmicpc.net/problem/20046
# 접근 방법
# 다익스트라 최단경로 알고리즘을 활용해 값을 갱신한다.
def dijkstra(r, c):
    if road[r][c] == -1:
        return
    cost[r][c] = road[r][c]
    q = []
    heapq.heappush(q, [cost[r][c], r, c])
    while q:
        co, r, c = heapq.heappop(q)
        if cost[r][c] < co:
            continue
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if 0<=r+dr <= n-1 and 0<= c+dc<= m-1 and road[r+dr][c+dc] != -1 and cost[r+dr][c+dc] > co + road[r+dr][c+dc]:
                cost[r+dr][c+dc] = co + road[r+dr][c+dc]
                heapq.heappush(q, [cost[r+dr][c+dc], r+dr, c+dc])


import sys, heapq
input = sys.stdin.readline
n, m = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(n)]
INF = int(1e9)
cost = [[INF for _ in range(m)] for _ in range(n)]

dijkstra(0, 0)
if cost[n-1][m-1] == INF:
    print(-1)
else:
    print(cost[n-1][m-1])
