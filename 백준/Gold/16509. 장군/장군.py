# https://www.acmicpc.net/problem/16509
# 접근 방법
# 주어진 가능한 이동경로를 활용해 BFS를 써서 문제를 해결한다.
from collections import deque
N, M = 10, 9
visited = [[-1 for _ in range(M)] for _ in range(N)]
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

visited[r1][c1] = 0
queue = deque([])
queue.append([r1, c1])
while queue:
    r, c = queue.popleft()
    for dr, dc, check_r, check_c in [[3, 2, 2, 1], [3, -2, 2, -1], [-3, 2, -2, 1], [-3, -2, -2, -1], [2, 3, 1, 2], [-2, 3, -1, 2], [2, -3, 1, -2], [-2, -3, -1, -2]]:
        if 0<=r+dr<N and 0<=c+dc<M and visited[r+dr][c+dc] == -1 and (r+check_r != r2 or c+check_c != c2):
                visited[r+dr][c+dc] = visited[r][c] + 1
                queue.append([r+dr, c+dc])

print(visited[r2][c2])