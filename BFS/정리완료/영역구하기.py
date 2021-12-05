# 접근방법
# 직사각형의 꼭짓점을 입력받아, 좌표 평면상에 직사각형이 있는 위치를 그리고, BFS를 진행한다.
import sys
from collections import deque

m, n, k = map(int, sys.stdin.readline().split()) # 모눈 종이의 가로 세로 길이와 직사각형의 개수 입력받기
grid_paper = [[0 for _ in range(n)] for _ in range(m)] # 모눈 종이 구현하기
squares = [list(map(int, sys.stdin.readline().split())) for _ in range(k)] # 직사각형 정보 입력 받기
direction = [[1, 0], [-1, 0], [0, 1], [0, -1]] # 상하좌우에 대한 좌표

# 문제 예시와는 다르게 180도 회전한 모눈 종이의 모양이 나타난다. 시작점과 진행 방향이 다르기 때문
# 하지만 문제를 푸는 데에는 이상없다.

for left, bottom, right, top in squares:
    for x in range(left, right):
        for y in range(bottom, top):
            grid_paper[y][x] = 1
            # 직사각형이 있는 좌표를 1로 입력한다.

# BFS 함수
def bfs(x, y):
    grid_paper[y][x] = 1 # 입력파라미터로 입력된 x, y 좌표의 모눈 종이 방문 처리
    area = 1 # 방문한 장소의 너비 초기화

    queue = deque([])
    queue.append([x,  y])

    while queue: # 큐가 빌 때까지 진행

        x, y = queue.popleft()
        for dx, dy in direction:
            if 0<= x+dx <= n-1 and 0 <= y+dy <= m-1 and grid_paper[y+dy][x+dx] == 0: # 주어진 범위 이내인지와 해당 위치가 직사각형이 없는 지 파악
                grid_paper[y+dy][x+dx] = 1 # 방문 처리
                area += 1 # 방문한 장소의 너비를 더해주기
                queue.append([x+dx, y+dy])

    return area # 너비 리턴

count = 0 # 분리된 영역의 개수
area = [] # 너비 출력을 위한 리스트
for x in range(n):
    for y in range(m):
        if grid_paper[y][x] == 0:
            area.append(bfs(x, y))
            count += 1

area.sort() # 오름차순 정렬

print(count)
for x in area:
    print(x, end = ' ')