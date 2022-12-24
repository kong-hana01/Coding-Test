# https://www.acmicpc.net/problem/1326
# 접근 방법
# bfs로 문제를 해결한다.
from collections import deque
n = int(input())
arr = [0] + list(map(int, input().split()))
a, b = map(int, input().split())
queue = deque([])
queue.append(a)
visited = [-1 for _ in range(n+1)]
visited[a] = 0
while queue:
    now = queue.popleft()
    step = arr[now]
    next = now + step
    while next <= n:
        if visited[next] == -1:
            visited[next] = visited[now] + 1
            queue.append(next)
        next += step
        
    next = now - step
    while 1 <= next:
        if visited[next] == -1:
            visited[next] = visited[now] + 1
            queue.append(next)
        next -= step
    
print(visited[b])