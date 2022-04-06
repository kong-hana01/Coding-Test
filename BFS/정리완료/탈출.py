# https://www.acmicpc.net/problem/3055
# 접근방법
# BFS를 활용해 물과 고슴도치의 위치를 상하좌우로 한칸씩 움직인다.
# 단 물부터 먼저 움직이고, 고슴도치를 움직이고, 매 초마다 동작하도록 한다.
from collections import deque

r, c = map(int, input().split())
map_ = [[x for x in input()] for _ in range(r)]
hedgehog = deque([])
water = deque([])

for i in range(r):
    for j in range(c):
        if map_[i][j] == '*':
            water.append([i, j])
        elif map_[i][j] == 'S':
            hedgehog.append([i, j])
            map_[i][j] = 0
        elif map_[i][j] == 'D':
            x, y = i, j


def water_move():
    # 1초 마다 물 이동
    water_ = []
    while water:
        row, col = water.popleft()
        map_[row][col] = '*'
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if 0<=row+dr<=r-1 and 0<=col+dc<=c-1:
                if map_[row+dr][col+dc] in ['.', 'S'] and [row_dr, col+dc] not in water_:
                    water_.append([row+dr, col+dc])
                    

    # 물을 다 이동시킨 뒤, 새로운 장소를 다시 water에 입력
    while water_:
        x = water_.pop()
        water.append(x)
    

def hedgehog_move():
    # 1초마다 고슴도치 이동
    hedgehog_ = []
    while hedgehog:
        row, col = hedgehog.popleft()
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if 0<=row+dr<=r-1 and 0<=col+dc<=c-1:
                if map_[row+dr][col+dc] == '.' and [row+dr, col+dc] not in water:
                    hedgehog_.append([row+dr, col+dc])
                    map_[row+dr][col+dc] = map_[row][col] + 1
                elif map_[row+dr][col+dc] == 'D':
                    map_[row+dr][col+dc] = map_[row][col] + 1
                    return True

    # 고슴도치를 다 이동시킨 뒤, 새로운 자소를 다시 hedgehog에 입력
    while hedgehog_:
        x = hedgehog_.pop()
        hedgehog.append(x)

    return False

for time in range(1, 2501):
    if not hedgehog:
        break

    water_move()
    if hedgehog_move():
        break
if map_[x][y] == 'D':
    print('KAKTUS')
else:
    print(map_[x][y])