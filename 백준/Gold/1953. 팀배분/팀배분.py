# https://www.acmicpc.net/problem/1953
# 접근 방법
# bfs를 통해 팀 배분을 한다.
def bfs(start):
    queue = deque([])
    queue.append([start, 0])
    visited[start] = 0

    while queue:
        now, team = queue.popleft()
        if team == 1:
            blue.append(now)
        else:
            white.append(now)
        next_team = (team+1) % 2
        for next in graph[now]:
            if visited[next] == -1:
                visited[next] = next_team
                queue.append([next, next_team])

from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n+1)]
visited = [-1 for _ in range(n+1)]
blue = []
white = []
for i in range(1, n+1):
    graph[i] = list(map(int, input().split()))[1:]



for i in range(1, n+1):
    if visited[i] == -1:
        bfs(i)
blue.sort()
white.sort()
print(len(blue))
print(*blue)
print(len(white))
print(*white)