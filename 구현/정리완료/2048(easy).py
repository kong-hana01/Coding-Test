# https://www.acmicpc.net/problem/12100
# 접근방법
# 주어진 보드에서 상하좌우로 총 5번씩 움직인 뒤, 나타난 결과 중 가장 큰 블록을 출력한다.
# 시간복잡도: 400(보드의 크기) x 4 ^ 5 (상하좌우를 총 5번 움직였을 때의 경우의 수) = 최대 약 410만번의 연산
import sys
from itertools import product

n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def move(board):
    # board_ = [l[:] for l in board]
    for x in list(product([1, 2, 3, 4], repeat=5)):
        board_ = [l[:] for l in board]
        for i in x:
            if i == 1:
                move_right(board_)
            elif i == 2:
                move_left(board_)
            elif i == 3:
                move_up(board_)
            else:
                move_down(board_)
    # move_right(board_)
    # move_right(board_)
    # move_right(board_)
    # move_right(board_)
    # move_down(board_)


def move_right(board):
    global result

    for i in range(n):
        array = []
        for x in [x for x in board[i] if x > 0]: # 가로로 움직이는 경우
            array.append(x)
        j = 0
        while len(array) - 1 > j:
            if array[len(array) - 1 - j] == array[len(array) - 2 - j]: # 오른쪽으로 움직이는 경우 오른쪽을 기준으로 합친다.
                array[len(array) - 1 - j] *= 2
                array[len(array) - 2 - j] = 0
                j += 1
            j += 1
        
        array = [x for x in array if x > 0]
        board[i] = [0 for _ in range(n)]
        for j in range(len(array)):
            board[i][n - 1 - j] = array[len(array) - 1 - j]
            result = max(result, array[len(array) - 1 - j])
    


def move_left(board):
    global result

    for i in range(n):
        array = []
        for x in [x for x in board[i] if x > 0]: # 가로로 움직이는 경우
            array.append(x)
        j = 0
        while len(array) - 1 > j:
            if array[j] == array[j + 1]: # 왼쪽으로 움직이는 경우
                array[j] *= 2
                array[j + 1] = 0
                j += 1
            j += 1

        array = [x for x in array if x > 0]
        board[i] = [0 for _ in range(n)]
        for j in range(len(array)):
            board[i][j] = array[j]
            result = max(result, array[j])
    

def move_up(board):
    global result

    for i in range(n):
        array = []
        for j in range(n): # 세로로 움직이는 경우
            array.append(board[j][i])
        array = [x for x in array if x > 0]

        j = 0
        while len(array) - 1 > j:
            if array[j] == array[j + 1]: # 위쪽으로 움직이는 경우
                array[j] *= 2
                array[j + 1] = 0
                j += 1
            j += 1

        array = [x for x in array if x > 0]
        for j in range(n):
            board[j][i] = 0
        for j in range(len(array)):
            board[j][i] = array[j]
            result = max(result, array[j])



def move_down(board):
    global result
    
    for i in range(n):
        array = []
        for j in range(n): # 세로로 움직이는 경우
            array.append(board[j][i])
        array = [x for x in array if x > 0]
        j = 0
        while len(array) - 1 > j:
            if array[len(array) - 1 - j] == array[len(array) - 2 - j]: # 아래쪽으로 움직이는 경우 오른쪽을 기준으로 합친다.
                array[len(array) - 1 - j] *= 2
                array[len(array) - 2 - j] = 0
                j += 1
            j += 1
        array = [x for x in array if x > 0]
        for j in range(n):
            board[j][i] = 0
        for j in range(len(array)):
            board[n - 1 - j][i] = array[len(array) - 1 - j]
            result = max(result, array[len(array) - 1 - j])

result = 0
move(board)
print(result)