# https://www.acmicpc.net/problem/23324
# 접근 방법
# 다익스트라 최단경로 알고리즘을 활용해 최단경로를 구한다. 이때 구한 값을 활용해 집단을 나눈 뒤, 카디션곱을 할 때의 개수를 구한다.
def dijkstra():
    distance[1] = 0
    h = []
    heapq.heappush(h, [0, 1])
    while h:
        dist, now = heapq.heappop(h)
        if distance[now] < dist:
            continue
        for next, add in graph[now]:
            if distance[next] > dist + add:
                distance[next] = dist + add
                heapq.heappush(h, [dist+add, next])


import sys, heapq
input = sys.stdin.readline
n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n+1)]
for i in range(m):
    if i == k-1:
        graph[arr[i][0]].append([arr[i][1], 1])
        graph[arr[i][1]].append([arr[i][0], 1])
        continue
    graph[arr[i][0]].append([arr[i][1], 0])
    graph[arr[i][1]].append([arr[i][0], 0])
    
distance = [2 for _ in range(n+1)]
dijkstra()
print(distance.count(1) * distance.count(0))