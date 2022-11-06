# https://www.acmicpc.net/problem/24480
# 접근 방법
# DFS를 통해 문제를 해결한다.
def dfs(node):
    global cnt
    for next in graph[node]:
        if not visited[next]:
            cnt += 1
            visited[next] = cnt
            dfs(next)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))
n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n+1):
    graph[i].sort(reverse=True)

visited = [0 for _ in range(n+1)]
visited[r] = 1
cnt = 1
dfs(r)
for x in range(1, n+1):
    print(visited[x])