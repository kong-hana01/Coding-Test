# https://www.acmicpc.net/problem/1647
# 접근 방법
# 크루스칼 알고리즘을 사용해 최소스패닝 트리를 만든다.
def prim(start):
    total_cost = 0
    max_cost = 0
    h = []
    union_cnt = 1
    visited = [False for _ in range(n+1)]
    visited[start] = True
    for next, cost, i in graph[start]:
        heapq.heappush(h, [cost, i])
    while union_cnt < n:
        cost, i = heapq.heappop(h)
        now, last, cost = edge[i]
        if not find_union(now, last):
            continue
        if visited[now]:
            last, now = now, last
        
        visited[now] = True
        total_cost += cost
        union_cnt += 1
        if max_cost < cost:
            max_cost = cost
        
        for next, cost, i in graph[now]:
            if now == get_union(next):
                continue
            heapq.heappush(h, [cost, i])
    return total_cost - max_cost

def get_union(node):
    if union[node] == node:
        return node
    union[node] = get_union(union[node])
    return union[node]

def find_union(n1, n2):
    n1 = get_union(n1)
    n2 = get_union(n2)
    if n1 != n2:
        union[n1] = n2
        return True
    return False

import sys, heapq
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
union = [i for i in range(n+1)]
edge = [tuple(map(int, input().split())) for _ in range(m)]
edge.sort(key=lambda x: x[2], reverse=True)
for i in range(m):
    a, b, c = edge[i]
    graph[a].append([b, c, i])
    graph[b].append([a, c, i])

result = 0
max_cost = 0
cnt_of_unions = 0
while cnt_of_unions < n-1:
    a, b, c = edge.pop()
    if get_union(a) != get_union(b):
        find_union(a, b)
        cnt_of_unions += 1
        result += c
        max_cost = max(max_cost, c)
print(result - max_cost)