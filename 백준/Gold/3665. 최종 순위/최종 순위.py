# https://www.acmicpc.net/problem/3665
# 접근 방법
def swap(a, b):
    if a in graph[b]:
        a, b = b, a
    graph[a].remove(b)
    graph[b].add(a)
    indegree[a] += 1
    indegree[b] -= 1

import sys, heapq
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    n = int(input())
    arr = list(map(int, input().split()))     
    indegree = [0 for _ in range(n+1)]
    graph = [set([]) for _ in range(n+1)]
    for i in range(n):
        x = arr[i]
        for j in range(i+1, n):
            y = arr[j]
            graph[x].add(y)
            indegree[y] += 1
    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        swap(a, b)
    
    h = []
    rank = []
    for i in range(1, n+1):
        if indegree[i] == 0: heapq.heappush(h, i)
    
    while len(h) == 1:
        now = heapq.heappop(h)
        rank.append(now)
        for next in graph[now]:
            indegree[next] -= 1
            if indegree[next] == 0: heapq.heappush(h, next)
    
    if len(h) != 0:
        print("?")
    elif len(rank) != n:
        print("IMPOSSIBLE")
    else:
        print(*rank)