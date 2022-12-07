# https://www.acmicpc.net/problem/7569
# 접근 방법
# 주어진 방향 조건대로 BFS를 돌려가며 며칠이 지나면 토마토가 모두 익는 지 확인한다.
# 단, 모두 익지 못하는 상황을 확인하기 위해 익지 않은 토마토의 개수를 세어주고, 이에 따라 0, -1, 토마토가 익을 때까지 걸리는 날짜를 계산해 출력한다.
from collections import deque
m, n, h = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
count = 0
queue = deque([])
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 0:
                count += 1
            elif box[i][j][k] == 1:
                queue.append([i,j,k])

result = 0
while queue and count:
    height, row, col = queue.popleft()
    for dh, dr, dc in [[0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1], [1, 0, 0], [-1, 0, 0]]:
        if 0<=height+dh<h and 0<=row+dr<n and 0<=col+dc<m and box[height+dh][row+dr][col+dc] == 0:
            box[height+dh][row+dr][col+dc] = box[height][row][col] + 1
            result = max(result, box[height][row][col])
            queue.append([height+dh, row+dr, col+dc])
            count -= 1
    
if count:
    print(-1)
else:
    print(result)