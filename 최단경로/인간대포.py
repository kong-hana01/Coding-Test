# https://www.acmicpc.net/problem/10473
# 접근 방법
# 0. 다익스트라 최단경로를 통해 각 대포까지 가는 가는 최단 시간을 계산한다.
# 1. 모든 대포의 최단경로를 갱신한 뒤, 각 대포나 시작 위치에서 목적지까지의 시간을 계산하여 최솟값을 출력한다.
def dijkstra():
    while h:
        dist, now = heapq.heappop(h)
        if dist > distance[now]:
            continue
        x1, y1 = cannon[now]
        for i in range(n+1):
            if i == now:
                continue
            x2, y2 = cannon[i]
            distAB = math.sqrt((x1-x2)**2 + (y1-y2)**2)
            minTime = min(distAB, abs(50-distAB)+10, abs(distAB-50)+10) / 5
            if minTime + distance[now] < distance[i]:
                distance[i] = minTime + distance[now] 
                heapq.heappush(h, [distance[i], i])

import heapq, math
start = list(map(float, input().split()))
end = list(map(float, input().split()))
n = int(input())
cannon = [list(map(float, input().split())) for _ in range(n)] + [end]
INF = int(1e9)
x1, y1 = start
distance = [math.sqrt((x1-x2)**2 + (y1-y2)**2) / 5 for x2, y2 in cannon]
h = []
for i in range(n+1):
    heapq.heappush(h, [distance[i], i])
dijkstra()
print(distance[-1])