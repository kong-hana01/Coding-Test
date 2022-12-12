# https://www.acmicpc.net/problem/12869
# 접근 방법
# bfs로 문제를 해결한다.

from collections import deque

n = int(input())
scvs = list(map(int, input().split()))
if n == 1:
    scvs = scvs + [0, 0]
elif n == 2:
    scvs = scvs + [0]

visited = [[[-1 for _ in range(61)] for _ in range(61)] for _ in range(61)]
queue = deque([])
queue.append(scvs)
visited[scvs[0]][scvs[1]][scvs[2]] = 0
while queue:
    s1, s2, s3 = queue.popleft()
    for n1, n2, n3 in [[s1-9, s2-3, s3-1], [s1-3, s2-9, s3-1], [s1-9, s2-1, s3-3], [s1-3, s2-1, s3-9], [s1-1, s2-9, s3-3], [s1-1, s2-3, s3-9]]:
        n1 = max(0, n1)
        n2 = max(0, n2)
        n3 = max(0, n3)
        if visited[n1][n2][n3] == -1:
            visited[n1][n2][n3] = visited[s1][s2][s3] + 1
            queue.append([n1, n2, n3])
print(visited[0][0][0])