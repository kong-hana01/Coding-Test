# https://www.acmicpc.net/problem/17144
# 접근 방법
# 1. 매 초마다 모든 미세먼지가 상하좌우로 확산되고 남은 미세먼지는 그 위치에 남는다.
# 1-1. 이를 확산시킬 때 모든 미세먼지가 퍼지고 난 뒤에 남은 미세먼지와 합쳐야지 제대로 된 확산이 이루어진다.
# 최대 연산 횟수: 칸의 개수 x 시간 x (상하좌우 연산 + 남은 미세먼지)= 50 x 50 x 1000 x 5 = 약 1250만번 이하(미세먼지 위치와 처음 주어지는 미세먼지의 양이 1000개이므로 이보다 적음)
# 2. 공기청정기가 순환하는 바람의 방향의 제일 끝부터 탐색을 진행하며 인덱스의 값을 한칸씩 이동시킨다.
# 최대 연산 횟수: 가로 세로 최대 길이 x 6 x 시간 = 50 x 6 x 1000 = 300,000회

import sys
r, c, t = map(int, sys.stdin.readline().split())
room = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]
total_dust = 0
top_wind = [] # 윗 바람 방향의 역순 위치 저장
bottom_wind = [] # 아랫 바람 방향의 역순 위치 저장
for row in range(r):
    for col in range(c):
        if room[row][col] > 0:
            total_dust += room[row][col]
        elif room[row][col] == -1:
            i = row
            j = col
            if not top_wind:
                while i > 0:
                    i -= 1
                    top_wind.append([i, j])
                while j < c-1:
                    j += 1
                    top_wind.append([i, j])
                while i < row:
                    i += 1
                    top_wind.append([i, j])
                while j > col + 1:
                    j -= 1
                    top_wind.append([i, j])
            else:
                while i < r-1:
                    i += 1
                    bottom_wind.append([i, j])
                while j < c-1:
                    j += 1
                    bottom_wind.append([i, j])
                while i > row:
                    i -= 1
                    bottom_wind.append([i, j])
                while j > col + 1:
                    j -= 1
                    bottom_wind.append([i, j])

def dust_diffusion(r, c):
    room_ = [[0 for _ in range(c)] for _ in range(r)]
    for row in range(r):
        for col in range(c):
            if room[row][col] > 0:
                count = 0
                for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    if 0<=row+dr<=r-1 and 0<=col+dc<=c-1 and room[row+dr][col+dc] >= 0:
                        room_[row+dr][col+dc] += room[row][col] // 5
                        count += 1
                room[row][col] = room[row][col] - ((room[row][col] // 5) * count)

    for row in range(r):
        for col in range(c):
            room[row][col] += room_[row][col]


def working_air_cleaner():
    global total_dust
    row, col = top_wind[0]
    total_dust -= room[row][col]
    room[row][col] = 0

    for i in range(1, len(top_wind)):
        row1, col1 = top_wind[i-1]
        row2, col2 = top_wind[i]
        room[row1][col1] = room[row2][col2]
        room[row2][col2] = 0

    row, col = bottom_wind[0]
    total_dust -= room[row][col]
    room[row][col] = 0

    for i in range(1, len(bottom_wind)):
        row1, col1 = bottom_wind[i-1]
        row2, col2 = bottom_wind[i]
        room[row1][col1] = room[row2][col2]
        room[row2][col2] = 0

for sec in range(t):
    dust_diffusion(r, c)
    working_air_cleaner()

print(total_dust)