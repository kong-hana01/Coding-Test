# https://www.acmicpc.net/problem/1766
# 접근 방법
# 최소 힙을 사용해 위상정렬을 구현하여 위의 문제를 해결한다.
import heapq, sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

h = [] # 진입차수가 0인 문제 번호
for i in range(1, n+1):
    if not indegree[i]: heapq.heappush(h, i)

result = []
while h:
    num = heapq.heappop(h)
    result.append(num)
    for x in graph[num]:
        indegree[x] -= 1
        if not indegree[x]: heapq.heappush(h, x)
print(*result)