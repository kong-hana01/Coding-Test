import sys
sys.setrecursionlimit(500000)
n, m = map(int, sys.stdin.readline().split())
array = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
#n, m = 6, 5
#array = [[1, 2], [2, 5], [5, 1], [3, 4], [4, 6]]
visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]
for x, y in array:
    graph[x].append(y)
    graph[y].append(x)

def dfs(i):
    visited[i] = True

    for x in graph[i]:
        if not visited[x]:
            dfs(x)

count = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        count += 1
print(count)