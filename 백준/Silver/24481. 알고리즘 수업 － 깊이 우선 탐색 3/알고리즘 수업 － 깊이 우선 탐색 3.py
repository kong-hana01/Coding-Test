# https://www.acmicpc.net/problem/24481
def dfs(node, depth):
    visited[node] = depth
    for next in graph[node]:
        if visited[next] == -1:
            dfs(next, depth+1)


import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline
n, m, r = map(int, input().split())
visited = [-1 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n+1):
    graph[i].sort()

depth = 0
dfs(r, depth)
for i in range(1, n+1):
    print(visited[i])