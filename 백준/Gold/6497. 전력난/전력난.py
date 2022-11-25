# https://www.acmicpc.net/problem/6497
# 접근 방법
# 최소 스패닝 트리를 구해 문제를 해결한다.
import heapq, sys
input = sys.stdin.readline
while True:
    m, n = map(int, input().split())
    if m == n == 0:
        break
    graph = [[] for _ in range(m)]
    visited = set([])
    h = []
    total_dist = 0
    for _ in range(n):
        x, y, z = map(int, input().split())
        graph[x].append([y, z])
        graph[y].append([x, z])
        total_dist += z

    # 힙 초기화
    for next, dist in graph[0]:
        heapq.heappush(h, [dist, next])
    visited.add(0)
    reduced_dist = 0
    
    # 프림
    while len(visited) < m:
        dist, now = heapq.heappop(h)
        if now in visited:
            continue
        visited.add(now)
        reduced_dist += dist
        for next, dist in graph[now]:
            if next not in visited:
                heapq.heappush(h, [dist, next])
    print(total_dist - reduced_dist)