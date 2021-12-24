# 접근 방법
# 다익스트라 최단경로 알고리즘을 통해 한 컴퓨터로부터 해킹할 수 있는 컴퓨터개수와 그 최대 시간을 출력한다.
def dijkstra(start):
    time[start] = 0
    q = []
    heapq.heappush(q, [0, start])
    while q:
        t, now = heapq.heappop(q)
        if time[now] < t:
            continue
        
        for next, sec in graph[now]:
            cost = t + sec
            if time[next] > cost:
                heapq.heappush(q, [cost, next])
                time[next] = cost


import heapq, sys
input = sys.stdin.readline
for tc in range(int(input())):
    n, d, c = map(int, input().split())
    INF = int(1e9)
    time = [INF for _ in range(n+1)]
    graph =[[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append([a, s])
    
    dijkstra(c)
    print(sum(1 for x in time if x < INF), max([x for x in time if x <INF]))
    