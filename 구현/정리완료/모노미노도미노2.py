# https://www.acmicpc.net/problem/20061
# 접근 방법
# 0. 빨간색 타일에 블록을 놓고, 이를 파란색 타일, 초록색 타일에 옮기는 함수, 점수를 획득하고 타일을 없애는 함수, 연한 칸에 블록이 있으면 가장 끝 행 또는 열을 없애는 함수, 행또는 열을 하나씩 옮기는 함수를 만든다.
# 1. 블록을 놓는 함수
# 1-1. 초록색 타일과 파란색 타일에 해당하는 리스트를 만든다.
# 1-2. 주어진 위치에 대해 초록색 타일은 열을 기준으로 0행부터 하나씩 탐색해가며 블록을 놓을 수 있는 최대한 높은 행에 블록(1)을 놓는다.
# 1-3. 파란색 타일은 행을 기준으로 0열부터 하나씩 탐색해가며 블록을 놓을 수 있는 최대한 번호가 높은 열에 블록을 놓는다.
# 2. 점수를 획득하고 타일을 없애는 함수
# 2-1. 초록색 타일과 파란색 타일을 행 또는 열별로 탐색하며 모든 행 또는 열에 1의 값이 있다면 해당 타일을 없애고 점수를 1점 획득한 뒤, 블록의 행 또는 열을 하나씩 이동시킨다.
# 3. 연한 칸에 블록이 있으면 가장 끝 행 또는 열을 없애는 함수
# 3-1. 연한 칸에 블록이 있는지 확인한 뒤, 있다면 블록의 행 또는 열을 하나씩 이동시킨다.
# 4. 블록의 행 또는 열을 하나씩 옮기는 함수
# 4-1. 타일의 종류에 따라 인덱스를 활용해 블록의 위치를 조정한다.
import sys
input = sys.stdin.readline
blue = [[0 for _ in range(6)] for _ in range(4)]
green = [[0 for _ in range(4)] for _ in range(6)]
score = 0
def place_block(t, x, y):
    place = []
    min_index_g = 5
    min_index_b = 5
    if t == 1:
        place.append([x, y])
    elif t == 2:
        place.append([x, y])
        place.append([x, y+1])
        min_index_b = 4
    else:
        place.append([x, y])
        place.append([x+1, y])
        min_index_g = 4
    
    for i in range(6): # 초록색 타일
        for r, c in place:
            r_ = r-x+i
            if r_ < 6 and green[r_][c] == 1:
                min_index_g = min(min_index_g, i-1)
    
    for r, c in place:
        i = r-x+min_index_g
        green[i][c] = 1

    for i in range(6): # 파란색 타일
        for r, c in place:
            c_ = c-y+i
            if c_ < 6 and blue[r][c_] == 1:
                min_index_b = min(min_index_b, i-1)
    
    for r, c in place:
        i = c-y+min_index_b
        blue[r][i] = 1
    

def move_block(blue, green, move):
    for tile, index in move:
        if tile == 0:
            green = [[green[i-1][j] if 0 < i <= index else green[i][j] for j in range(4)] for i in range(6)]
            for i in range(4):
                green[0][i] = 0
        else:
            blue = [[blue[i][j-1] if 0 < j <= index else blue[i][j] for j in range(6)] for i in range(4)]
            for i in range(4):
                blue[i][0] = 0

    return green, blue

def calc_score(blue, green):
    global score
    
    move = []
    for i in range(6): # 초록색 타일
        if 1 == green[i][0] == green[i][1] == green[i][2] == green[i][3]:
            for j in range(4):
                green[i][j] = 0
            score += 1
            move.append([0, i])
    
    for i in range(6): # 파란색 타일
        if 1 == blue[0][i] == blue[1][i] == blue[2][i] == blue[3][i]:
            for j in range(4):
                blue[j][i] = 0
            score += 1
            move.append([1, i])
    
    green, blue = move_block(blue, green, move)
    return green, blue

def search_light_color(blue, green):
    move = []
    for i in range(2):
        for j in range(4):
            if green[i][j]:
                move.append([0, 5])
                break

    for i in range(2):
        for j in range(4):
            if blue[j][i]:
                move.append([1, 5])
                break
    green, blue = move_block(blue, green, move)
    return green, blue

n = int(input())
for _ in range(n):
    t, x, y = map(int, input().split())
    place_block(t, x, y)
    green, blue = calc_score(blue, green)
    green, blue = search_light_color(blue, green)

block_count = 0
for i in range(6):
    for j in range(4):
        block_count += green[i][j]
        block_count += blue[j][i]
        
print(score)
print(block_count)