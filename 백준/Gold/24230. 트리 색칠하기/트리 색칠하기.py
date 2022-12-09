# https://www.acmicpc.net/problem/24230
# 접근 방법
# DFS를 활용할 때 현재 노드의 색깔과 전달받은 색깔이 다르다면 이를 바꿔주고, 개수를 늘려서 답을 구한다.
def dfs(now, color):
    global result
    visited[now] = True
    for next in graph[now]:
        if not visited[next]:
            if arr[next] != color:
                result += 1
            dfs(next, arr[next])

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
arr = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
graph[0].append(1)
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = 0
dfs(0, 0)
print(result)