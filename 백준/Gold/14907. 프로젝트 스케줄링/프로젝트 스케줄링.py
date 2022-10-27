 # https://www.acmicpc.net/problem/14907
 # 접근방법
 # 위상정렬을 활용해 한 작업까지 오는 데의 걸리는 최대 시간을 계산하고, 이를 기준으로 프로젝트의 최소 시간을 계산한다.
from re import L
import sys
from collections import deque
lines = sys.stdin.readlines()
# lines = []
# for _ in range(6):
#     lines.append(input())
indegree = {chr(alpha): 0 for alpha in range(ord('A'), ord('Z')+1)}
elapsed_time = {chr(alpha): 0 for alpha in range(ord('A'), ord('Z')+1)}
work = {chr(alpha): 0 for alpha in range(ord('A'), ord('Z')+1)}
graph = {chr(alpha): [] for alpha in range(ord('A'), ord('Z')+1)}
queue = deque([])
for line in lines:
    l = line.split()
    if len(l) == 2:
        alpha, now = l
        work[alpha] = int(now)
        queue.append(alpha)
        elapsed_time[alpha] = int(now)

    else:
        alpha, now, indegree_alpha = l
        indegree[alpha] = len(indegree_alpha)
        work[alpha] = int(now)
        for next_alpha in indegree_alpha:
            graph[next_alpha].append(alpha)

result = 0
while queue:
    now = queue.popleft()
    for next in graph[now]:
        elapsed_time[next] = max(elapsed_time[next], elapsed_time[now]+work[next])
        indegree[next] -= 1
        result = max(result, elapsed_time[next])
        if indegree[next] == 0:
            queue.append(next)

print(max(elapsed_time.values()))