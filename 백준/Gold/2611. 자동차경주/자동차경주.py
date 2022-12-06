# https://www.acmicpc.net/problem/2611
# 접근 방법
# 위상정렬을 사용하여, indegree가 0일 때 가장 높은 값을 기준으로 이를 처리한다.
# 첫 값은 1을 기준으로 엣지가 존재하는 경로에서부터 시작한다.
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
score = [0 for _ in range(n+1)]
path = [[] for _ in range(n+1)]
# 그래프 구성 및 진입차수 초기화
m = int(input())
for _ in range(m):
    p, q, r = map(int, input().split())
    if p == 1:
        score[q] = r
        continue
    graph[p].append([q, r])
    indegree[q] += 1

# 진입차수가 0인 노드 탐색(1부터 연결된 경로)
queue = deque([])
for i in range(1, n+1):
    if not indegree[i]:
        queue.append(i)
        path[i] = [1]

# 위상 정렬 수행
while queue:
    now = queue.popleft()
    path[now].append(now)

    for next, r in graph[now]:
        if score[next] < score[now] + r:
            score[next] = score[now] + r
            path[next] = path[now][:]

        indegree[next] -= 1
        if not indegree[next]:
            queue.append(next)

print(score[1])
print(*path[1])