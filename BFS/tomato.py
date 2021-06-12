import sys
from collections import deque
m, n = map(int,sys.stdin.readline().split())
#box_ = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1]]
box_ = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
step_ = [[1, 0], [-1, 0], [0, 1], [0, -1]]

# 시작지점을 하나씩 돌려가면서 box_를 채워갈 경우 최대 n x m만큼 bfs를 작동시켜야할 수 있음
# 따라서 1이 있는 위치부터 모두 큐에 넣고 시작한 뒤, 이를 하나씩 확장시키며 작동시킨다.
count = 0
queue = deque()
days = 0

for i in range(n):
    for j in range(m):
        if box_[i][j] == 1:
            queue.append([i, j])
        elif box_[i][j] == 0:
            count += 1

if count > 0:
    while queue:
        x, y = queue.popleft()
        for dx, dy in step_:
            if 0 <= x+dx <= n-1 and 0 <= y+dy <= m-1 and box_[x+dx][y+dy] == 0:
                queue.append([x+dx, y+dy])
                box_[x+dx][y+dy] = box_[x][y] + 1
                count -= 1
                days = box_[x][y]
    if count > 0:
        print(-1)
    else:
        print(days)
        
else:
    print(0)

#print(box_)