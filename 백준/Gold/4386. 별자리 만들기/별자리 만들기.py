# https://www.acmicpc.net/problem/4386
# 접근 방법
# 1. 각 별에 대해 모든 엣지를 만들어 완전 그래프 형태로 만든다.
# 2. 완전 그래프에 대해 힙을 사용해 최소 스패닝트리를 만든다.
import math, heapq
n = int(input())
distance = [[0 for _ in range(n+1)] for _ in range(n+1)]
locations = [[] for _ in range(n+1)]
for i in range(1, n+1):
    x, y = map(float, input().split())
    locations[i] = [x, y]

for i in range(1, n+1):
    x1, y1 = locations[i]
    for j in range(i+1, n+1):
        x2, y2 = locations[j]
        dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
        distance[i][j] = dist
        distance[j][i] = dist


result = 0
visited = [False for _ in range(n+1)]
visited[1] = True
h = []
for i in range(2, n+1):
    heapq.heappush(h, [distance[1][i], i])

cnt = 0
while cnt < n-1:
    dist, now = heapq.heappop(h)
    if visited[now]:
        continue
    cnt += 1
    result += dist
    visited[now] = True
    for next in range(2, n+1):
        if not visited[next]:
            heapq.heappush(h, [distance[now][next], next])

print(result)