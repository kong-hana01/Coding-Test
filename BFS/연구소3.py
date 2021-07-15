# https://www.acmicpc.net/problem/17142
# 접근방법
# 모든 바이러스를 놓을 수 있는 위치에 대해 바이러스를 활성화한 뒤, 각 경우의 수마다 BFS를 실행하며 모든 빈칸에 바이러스가 있게되는 최소 시간을 출력한다.
# 시간복잡도
# 최대연산횟수: 50(연구소 가로 크기) x 50(연구소 세로 크기) x 252(바이러스가 존재할 수 있는 위치에 바이러스를 놓는 경우의 수 중 최대값(1 <= M <= 바이러스를 놓을 수 있는 위치 <= 10)) = 약 63만번

from itertools import combinations
from collections import deque

# 바이러스가 존재할 수 있는 위치에 바이러스를 놓는 경우의 수 중 최대값 확인
max_calculation = 0
for i in range(1, 11):
    countOfvirus = len(list(combinations([x for x in range(1, 11)], i)))
    max_calculation = max(max_calculation, countOfvirus)
# print(max_calculation)


# 문제 풀이
n, m = map(int, input().split())
lab = [list(input().split()) for _ in range(n)]
# lab = [['2' if x == 2 else '0' for x in range(n)] for _ in range(n)]
direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

place = 0
placeOfvirus = []
for i in range(n):
    for j in range(n):
        if lab[i][j] == '2':
            placeOfvirus.append([i, j])
        elif lab[i][j] == '0':
            place += 1
# print(placeOfvirus)


min_time = 2500
for virus in list(combinations(placeOfvirus, m)): # 바이러스가 놓일 수 있는 모든 경우의 수
    lab_ = [l[:] for l in lab]
    queue = deque([])

    for x in virus:
        queue.append(x) # 해당 위치를 큐에 삽입
        lab_[x[0]][x[1]] = 0
    
    time = 0
    count = 0
    while queue: # BFS 진행
        x, y = queue.popleft()
        for dx, dy in direction:
            if 0<=x+dx<=n-1 and 0<=y+dy<=n-1:
                if lab_[x+dx][y+dy] =='0':
                    queue.append([x+dx, y+dy])
                    lab_[x+dx][y+dy] = lab_[x][y] + 1
                    time = lab_[x+dx][y+dy] # 항상 최대값으로 저장
                    count += 1
                    
                elif lab_[x+dx][y+dy] == '2':
                    queue.append([x+dx, y+dy])
                    lab_[x+dx][y+dy] = lab_[x][y] + 1
                    
        if place == count:
            min_time = min(min_time, time)
            break
        elif min_time < time:
            break
    
if min_time == 2500:
    print(-1)
else:
    print(min_time)