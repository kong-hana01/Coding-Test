# https://www.acmicpc.net/problem/14284
# 접근방법
# 다익스트라 최단경로 알고리즘과 분리집합을 사용해 알고리즘을 구현한다.
def get_parent(idx):
    if parent[idx] == idx:
        return idx
    parent[idx] = get_parent(parent[idx])
    return parent[idx]

def find_union(x1, x2):
    x1 = get_parent(x1)
    x2 = get_parent(x2)
    if x1 > x2:
        parent[x1] = x2
    else:
        parent[x2] = x1

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, [0, start])

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for x in graph[now]:
            cost = dist + x[1]
            if distance[x[0]] > cost:
                heapq.heappush(q, [cost, x[0]])
                distance[x[0]] = cost




import sys, heapq
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(m)]
s, t = map(int, input().split())
graph = [[] for _ in range(n+1)]
parent = [i for i in range(n+1)]
for a, b, c in array:
    find_union(a, b)
    graph[a].append([b, c])
    graph[b].append([a, c])
    if s == t:
        break
INF = int(1e9)
distance = [INF for _ in range(n+1)]
dijkstra(s)
print(distance[t])