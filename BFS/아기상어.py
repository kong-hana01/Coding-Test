# https://www.acmicpc.net/problem/16236
# 접근방법
# 주어진 조건에 따라 코드를 설계한다.

import sys
from collections import deque
n = int(input())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)] # 방문 처리를 위한 그래프 초기화
direction = [[-1, 0], [0, -1], [0, 1], [1, 0]] # 위, 왼쪽부터 탐색
size = 2 # 상어의 크기 초기화
count = 0 # 먹은 횟수 초기화

queue = deque([])
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            queue.append([i, j]) # 아기 상어의 위치 저장
            visited[i][j] = 1    
            graph[i][j] = 0

result = 0
t = 400
while queue:
    x, y = queue.popleft()

    for dx, dy in direction:
        # print(x+dx, y+dy)
        if 0<= x+dx <=n-1 and 0<= y+dy <=n-1 and graph[x+dx][y+dy] <= size and visited[x+dx][y+dy] == 0:
            
            if 0 < graph[x+dx][y+dy] < size: # 상어가 먹을 수 있는 크기라면
                # count += 1 # 먹은 횟수 증가
                t = min(t, visited[x][y] + 1)
            visited[x+dx][y+dy] = visited[x][y] + 1
            queue.append([x+dx, y+dy])
            # print('col:', x+dx+1)
            # print('row:', y+dy+1)
            
    if not queue:
        for x_ in range(n):
            for y_ in range(n):                    
                if 0 < graph[x_][y_] < size and visited[x_][y_] == t: # 상어가 먹을 수 있는 크기라면
                    count += 1 # 먹은 횟수 증가
                    
                    if count == size: # 상어가 물고기를 먹은 횟수와 크기가 같다면 사이즈 증가
                        size += 1
                        count = 0

                    # print(f'{visited[x_][y_]-1}초 소요, col: {x_+1}, row: {y_+1}')
                    result += t - 1 # 몇 초가 걸렸는지 체크
                    visited = [[0 for _ in range(n)] for _ in range(n)] # 방문 처리 초기화
                    graph[x_][y_] = 0
                    visited[x_][y_] = 1
                    queue.append([x_, y_])
                    t = 400
                    break

print(result)