# https://www.acmicpc.net/problem/14217
# 접근 방법
# 매 갱신마다 그래프에 추가를 해가며 이를 처리한다.
def bfs(v):
    visited[v] = 0
    queue = deque([])
    queue.append(v)
    while queue:
        now = queue.popleft()
        for next in graph[now]:
            if visited[next] == -1:
                visited[next] = visited[now] + 1
                queue.append(next)

from collections import deque
n, m = map(int, input().split())
graph = [set([]) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)
q = int(input())
for _ in range(q):
    visited = [-1 for _ in range(n+1)]
    a, i, j = map(int, input().split())
    if a == 1:
        graph[i].add(j)
        graph[j].add(i)
    else:
        graph[i].remove(j)
        graph[j].remove(i)
    bfs(1)
    print(*visited[1:])