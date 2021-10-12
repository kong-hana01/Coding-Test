# https://www.acmicpc.net/problem/19236
# 접근 방법
# 재귀적으로 각 공간에 대한 정보를 카피해가며 상어가 먹을 수 있는 물고기 번호의 최댓값을 구한다.
import sys
sys.setrecursionlimit(10**6)
board = [[0 for _ in range(4)] for _ in range(4)]
direction = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]
fish_direction = [0 for _ in range(17)]
fish_place = [[] for _ in range(17)]
for i in range(4):
    temp = list(map(int, input().split()))
    for j in range(4):
        board[i][j] = temp[j*2]
        fish_direction[temp[j*2]] = temp[j*2 + 1] - 1
        fish_place[temp[j*2]] = [i, j]
result = 0
feed_num = board[0][0]
fish_direction[0] = fish_direction[feed_num]
fish_place[feed_num] = 0
fish_place[0] = [0, 0]
board[0][0] = -1
def move(board_, fish_place_, fish_direction_):
    for num in range(1, 17):
        move_check = False
        if not fish_place_[num]:
            continue
        for _ in range(8):
            dr, dc = direction[fish_direction_[num]]
            r, c = fish_place_[num]
            if 0<=r+dr<=3 and 0<=c+dc<=3 and board_[r+dr][c+dc] != -1:
                move_check = True
                break
            fish_direction_[num] = (fish_direction_[num] + 1) % 8
        
        if move_check:
            num2 = board_[r+dr][c+dc]
            board_[r+dr][c+dc], board_[r][c] = board_[r][c], board_[r+dr][c+dc]
            fish_place_[num], fish_place_[num2] = fish_place_[num2], fish_place_[num]
    
    return board_

def feed(b, fish_place, fish_direction, total_sum):
    global result
    r, c = fish_place[0]
    dr, dc = direction[fish_direction[0]]
    for i in range(1, 4):
        temp_sum = total_sum
        if 0<=r+dr*i<=3 and 0<=c+dc*i<=3 and b[r+dr*i][c+dc*i]:
            board_ = [x[:] for x in b]
            fish_place_ = fish_place[:]
            fish_direction_ = fish_direction[:]
            feed_num = board_[r+dr*i][c+dc*i]
            board_[r+dr*i][c+dc*i] = -1
            board_[r][c] = 0
            fish_place_[0] = [r+dr*i, c+dc*i]
            print(r, c)
            print(fish_place_[0])
            print(board_)
            print(fish_direction_)
            print(feed_num)
            print()
            fish_place_[feed_num] = 0
            fish_direction_[0] = fish_direction_[feed_num]
            temp_sum += feed_num
            
            feed(move(board_, fish_place_, fish_direction_), fish_place_, fish_direction_, temp_sum)     
            return
    result = max(result, total_sum)

move(board, fish_place, fish_direction)
feed(board, fish_place, fish_direction, 0)
print(result)