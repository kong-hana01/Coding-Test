# https://www.acmicpc.net/problem/14676
# 접근 방법
# 위상정렬을 활용해 위의 문제를 해결한다.
from collections import deque
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
indegree = [0 for _ in range(n+1)] # 진입차수
graph = [[] for _ in range(n+1)] # 인덱스에 해당하는 건물이 지어져야 리스트 내의 건물을 지을 수 있음.
building = [0 for _ in range(n+1)] # 지금까지 지어진 건물
for _ in range(m):
    x, y = map(int, input().split())
    indegree[y] += 1
    graph[x].append(y)

queue = deque([])
for _ in range(k):
    commend, a = map(int, input().split())
    queue.append([commend, a])

visited = [False for _ in range(n+1)]
is_cheat = False
while queue and not is_cheat:
    commend, now = queue.popleft()
    if commend == 1:
        if indegree[now] != 0:
            is_cheat = True
            break
        building[now] += 1
        
        if not visited[now]:
            visited[now] = True
            
            for next in graph[now]:
                indegree[next] -= 1
    else:
        if building[now] == 0:
            is_cheat = True
            break
        building[now] -= 1
        if building[now] == 0:
            visited[now] = False
            for next in graph[now]:
                indegree[next] += 1

if is_cheat:
    print('Lier!')
else:
    print('King-God-Emperor')