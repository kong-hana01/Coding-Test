# https://www.acmicpc.net/problem/1939
# 접근 방법
# 최대힙을 사용해서 최대 중량을 계산한 뒤, 이를 출력한다.
def move(a):
    INF = int(1e9) + 1
    q = []
    heapq.heappush(q, [-INF, a])
    weight[a] = INF
    
    while q:
        w, now = heapq.heappop(q)
        if weight[now] > -w:
            continue
        for x in graph[now]:
            next_weight = min(-w, x[1])
            if next_weight > weight[x[0]]:
                heapq.heappush(q, [-next_weight, x[0]])
                weight[x[0]] = next_weight

import heapq, sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
a, b  = map(int, input().split())
weight = [0 for _ in range(n+1)]
move(a)
print(weight[b])