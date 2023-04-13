# https://www.acmicpc.net/problem/2479
# 접근 방법
# 각 코드마다 queue에 넣고, 이를 하나씩 뺀 다음 모든 코드에 대해 비교를 해보아서 A와 B 코드 사이의 경로인 경우에 queue에 넣는다.
def bfs(start, end):
    visited = [i for i in range(n)]
    queue = deque([])
    queue.append(start)
    while queue:
        now = queue.popleft()
        nowDifferentCount = calculateDifferentCount(now, end)
        for next in range(n):
            if visited[next] != next or calculateDifferentCount(now, next) != 1:
                continue
            queue.append(next)
            visited[next] = now
    return visited

def calculateDifferentCount(codeIdx1, codeIdx2):
    differentCount = 0
    for i in range(k):
        if codes[codeIdx1][i] != codes[codeIdx2][i]:
            differentCount += 1
    return differentCount

from collections import deque
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
codes = [input() for _ in range(n)]
a, b = map(lambda x: x-1, map(int, input().split()))
visited = bfs(a, b)
if visited[b] == b:
    print(-1)
else:
    result = [b+1]
    now = b
    while visited[now] != a:
        result.append(visited[now]+1)
        now = visited[now]
    result.append(a+1)
    print(*result[::-1])