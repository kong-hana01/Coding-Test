# https://www.acmicpc.net/problem/1916
# 접근 방법
# 전형적인 최단 경로 문제이므로 다익스트라 최단 경로를 우선순위 큐를 통해 구현한다.
import heapq, sys

def dijkstra(start):
    distance[start] = 0
    h = []
    heapq.heappush(h, [distance[start], start])

    while h:
        dist, now = heapq.heappop(h)
        if distance[now] < dist:
            continue
        for x in graph[now]:
            cost = dist + x[1]
            if cost < distance[x[0]]:
                heapq.heappush(h, [cost, x[0]])
                distance[x[0]] = cost


input = sys.stdin.readline
n = int(input())
m = int(input())
array = [list(map(int, input().split())) for _ in range(m)] # 출발 도시, 도착 도시, 비용
graph = [[] for _ in range(n+1)]
INF = int(1e9)
distance = [INF for _ in range(n+1)]
for i in range(m):
    departure, arrival, cost = array[i]
    graph[departure].append([arrival, cost])
start, end = map(int, input().split())

dijkstra(start)
print(distance[end])