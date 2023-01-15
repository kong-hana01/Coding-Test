# https://www.acmicpc.net/problem/14431
# 접근 방법
# 소수를 체크하고 이에 해당하는 값만 처리한다.
def dijkstra(s):
    h = []
    distance[s] = 0
    heapq.heappush(h, [0, s])
    while h:
        dist, now = heapq.heappop(h)
        x1, y1 = graph[now]
        if distance[now] < dist:
            continue
        for i in range(len(graph)):
            x2, y2 = graph[i]
            next_cost = int(math.sqrt((x1-x2) ** 2 + (y1-y2) ** 2))
            if prime_number[next_cost] == 0:
                continue
            if distance[i] < dist + next_cost:
                continue
            distance[i] = dist + next_cost
            heapq.heappush(h, [dist+next_cost, i])
        
import heapq, sys, math
input = sys.stdin.readline
prime_number = [-1 for _ in range(8500)]
prime_number[0], prime_number[1] = 0, 0
now = 2
while now < 8500:
    if prime_number[now] != -1:
        now += 1
        continue
    prime_number[now] = 1
    next = now * 2
    while next < 8500:
        prime_number[next] = 0
        next += now
    now += 1
x1, y1, x2, y2 = map(int, input().split())
n = int(input())
graph = [[x1, y1]] + [[] for _ in range(n)] + [[x2, y2]]
INF = int(1e8)
distance = [INF for _ in range(n+2)]
for i in range(1, n+1):
    x, y = map(int, input().split())
    graph[i] = [x, y]
dijkstra(0)
if distance[-1] == INF:
    print(-1)
else:
    print(distance[-1])