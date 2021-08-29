# https://www.acmicpc.net/problem/19237
# 접근방법
# 0. 격자 정보를 이중 리스트(board)로, 상어번호를 인덱스로 하는 방향 정보(now_direction)를 리스트로, 상어 번호를 인덱스로 하는 리스트에서 현재 방향에 따른 우선순위를 인덱스로 하는 삼중 리스트(direction)를 입력받는다.
# 1. 상어를 이동시킨 후엔 이동하기 전의 위치에 냄새를 남긴다. 단, 상어가 죽은 경우에도 냄새를 남긴다.
# 2. 모든 격자를 탐색하며 상어가 있는 경우에는 해당 상어를 현재 있는 상어 리스트에 삽입한 뒤, 우선순위에 따라 이동시킨다. 
# 2-1. 반복문을 통해 0부터 3까지 우선순위를 정해 direction에 입력 후, 해당 방향이 0일 경우 이를 멈추고 그 위치로 이동한다.
# 2-2. 만약 우선순위를 통해 탐색한 위치가 0이 아니지만 상어가 있다면 그 상어와의 번호를 비교해 더 낮은 번호의 상어만 남긴다.
# 2-3. 만약 모든 위치가 0이 아니고, 냄새가 있는 위치라면 상하좌우의 위치 중 본인의 냄새가 나는 위치로 다시 이동한다.
# 3. 상어의 이동이 끝난 뒤, 모든 격자를 탐색하며 냄새가 있는 정보의 k를 1씩 줄인다. 이때 k가 0이되면 해당 격자는 0으로 값을 바꾼다.(반복문의 특성을 이용해 순서대로 진행하지 않고, 1번과 3번을 함께 2번보다 선행되도록 함)
# 4. 1 ~ 3번이 끝나고 시간을 1초 증가시킨 뒤, 1 ~ 3번을 반복한다.
# 5. 1번 상어만 남게되면 모든 반복을 멈추고 몇 초가 지났는 지 출력한다.
# 6. 만약 1000초가 지났다면 반복을 멈추고 -1을 출력한다.

import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
now_direction = [0] # now_direction[상어번호]
direction = [[[] for _ in range(5)] for _ in range(m+1)] # direction[상어번호][현재방향(now_direction)][우선순위(0 ~ 3)]
for x in list(map(int, input().split())):
    now_direction.append(x)
    
for i in range(1, m+1):
    for j in range(1, 5):
        for x in list(map(int, input().split())):
            direction[i][j].append(x)

step = [[], [-1, 0], [1, 0], [0, -1], [0, 1]] # step[방향(direction)] -> 상하좌우에 대한 dx, dy


def move(r, c):
    shark = board[r][c][0]
    last_place = []
    # 2-1. 반복문을 통해 0부터 3까지 우선순위를 정해 direction에 입력 후, 해당 방향이 0일 경우 이를 멈추고 그 위치로 이동한다.
    for priority in range(4):
        dr, dc = step[direction[shark][now_direction[shark]][priority]]
        if 0<=r+dr<=n-1 and 0<=c+dc<=n-1:
            # 2-2. 만약 우선순위를 통해 탐색한 위치가 0이 아니지만 상어가 있다면 그 상어와의 번호를 비교해 더 낮은 번호의 상어만 남긴다.
            if type(board[r+dr][c+dc]) == type(0):
                
                shark_list.append([shark, r+dr, c+dc])
                last_place = []
                d = direction[shark][now_direction[shark]][priority]
                break

            elif board[r+dr][c+dc][0] == shark and not last_place:
                last_place.append([shark, r+dr, c+dc])
                d = direction[shark][now_direction[shark]][priority]
    
    # 2-3. 만약 모든 위치가 0이 아니고, 냄새가 있는 위치라면 상하좌우의 위치 중 본인의 냄새가 나는 위치로 다시 이동한다.
    if last_place:
        shark_list.append(last_place[0])

    now_direction[shark] = d

def smell():
    for r in range(n):
        for c in range(n):
            # 1. 상어를 이동하기 전에 냄새를 남긴다. 단, 상어가 죽은 경우에도 냄새를 남긴다.
            if type(board[r][c]) == type(0) and board[r][c] > 0:
                board[r][c] = [board[r][c], k]

            # 3. 상어의 이동이 끝난 뒤, 모든 격자를 탐색하며 냄새가 있는 정보의 k를 1씩 줄인다. 이때 k가 0이되면 해당 격자는 0으로 값을 바꾼다.
            elif type(board[r][c]) == type([]):
                board[r][c][1] -= 1
                if board[r][c][1] == 0:
                    board[r][c] = 0


time = 0
shark_count = 0
while shark_count != 1:
    if time >= 1000:
        time = -1
        break
    
    smell()
    shark_count = 0
    shark_list = []
    for r in range(n):
        for c in range(n):
            if type(board[r][c]) == type([]) and board[r][c][1] == k:
                move(r, c)
    
    for shark, r, c in shark_list:
        if board[r][c] == 0 or type(board[r][c]) != type(0):
            board[r][c] = shark
            shark_count += 1
        else:
            board[r][c] = min(board[r][c], shark)
    
    time += 1

print(time)
