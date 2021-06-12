import sys
#n, m = 5, 4
#array = [[0, 1], [1, 2], [2, 3], [3, 4]]

n, m = map(int, sys.stdin.readline().split())
array = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
graph = [[] for _ in range(n)]
for x, y in array:
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * n


def dfs(x, count=0):
    visited[x] = True
    if count == 4:
        print(1)
        exit()
    for data in graph[x]:
        if not visited[data]:
            dfs(data, count+1)
            visited[data] = False

for i in range(n):
    dfs(i)
    visited[i] = False

print(0)