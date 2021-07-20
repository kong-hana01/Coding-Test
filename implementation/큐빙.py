# https://www.acmicpc.net/problem/5373
# 접근 방법
# 어떤 면이 돌아갔을 때, 다른 면들이 어떻게 변하는 지를 파악한 뒤, 이를 반영하여 코드를 짠다.
# 1. 왼쪽 면이 돌아갔을 때
# - 시계방향인 경우: 윗면의 왼쪽 열 -> 앞면의 왼쪽 열 -> 아랫면의 왼쪽 열 -> 뒷면의 왼쪽 열 -> 윗면의 왼쪽 열 순으로 바뀐다.
# - 반시계방향인 경우: 윗면의 왼쪽 열 -> 뒷면의 왼쪽 열 -> 아랫면의 왼쪽 열 -> 앞면의 왼쪽 열 -> 윗면의 왼쪽 열 순으로 바뀐다.
# 2. 앞 면이 돌아갔을 때
# - 시계방향인 경우: 윗면의 아래 행 -> 오른쪽면의 왼쪽 열 -> 아랫면의 윗 행 -> 왼쪽면의 오른쪽 열 -> 윗면의 아래 행 순으로 바뀐다.
# - 반시계방향인 경우: 윗면의 아래 향 -> 왼쪽의 오른쪽 열 -> 아랫면의 윗 향 -> 오른쪽면의 왼쪽 열 -> 윗면의 아래 행 순으로 바뀐다.
# 3. 오른쪽 면이 돌아갔을 때
# - 시계방향인 경우: 윗면의 오른쪽 열 -> 뒷면의 오른쪽 열 -> 아랫면의 오른쪽 열 -> 앞면의 오른쪽 열 -> 윗면의 오른쪽 열 순으로 바뀐다.
# - 반시계방향인 경우: 윗면의 오른쪽 열 -> 앞면의 오른쪽 열 -> 아랫면의 오른쪽 열 -> 뒷면의 오른쪽 열 -> 윗면의 오른쪽 열 순으로 바뀐다.
# 4. 윗면이 돌아갔을 때
# - 시계방향인 경우: 왼쪽면의 윗 행 -> 뒷면의 아래행 -> 오른쪽면의 윗 행 -> 앞면의 윗행 순으로 바뀐다.
# - 반시계방향인 경우: 왼쪽면의 윗 행 -> 앞면의 윗 행 -> 오른쪽면의 윗행 -> 뒷면의 아래행 순으로 바뀐다.
# 5. 아래 면이 돌아갔을 때
# - 시계방향인 경우: 앞면의 아래 행 -> 오른쪽의 아래 행 -> 뒷면의 윗 행 -> 왼쪽면의 아래 행 -> 앞면의 아래 행
# - 반시계방향인 경우: 앞면의 아래 행 -> 왼쪽면의 아래행 -> 뒷면의 윗 행 -> 오른쪽면의 아래 행 -> 앞면의 아래 행
# 6. 뒷면이 돌아갔을 떄
# - 시계방향인 경우: 아래면의 아래 행 -> 오른쪽면의 오른쪽 행 -> 윗면의 윗 행 -> 왼쪽면의 왼쪽 행 -> 아래면의 아래 행
# - 반시계방향인 경우: 아래면의 아래 행 -> 왼쪽면의 왼쪽 행 -> 윗면의 윗 행 -> 오른쪽면의 오른쪽 행 -> 아래면의 아래 행
import sys


def cubing(order, direction):

    # 1. 왼쪽 면이 돌아갔을 때
    # - 시계방향인 경우: 윗면의 왼쪽 열 -> 앞면의 왼쪽 열 -> 아랫면의 왼쪽 열 -> 뒷면의 왼쪽 열 -> 윗면의 왼쪽 열(역) 순으로 바뀐다.
    # - 반시계방향인 경우: 윗면의 왼쪽 열 -> 뒷면의 왼쪽 열(역) -> 아랫면의 왼쪽 열 -> 앞면의 왼쪽 열 -> 윗면의 왼쪽 열 순으로 바뀐다.
    if order == 'L':
        front_, bottom_, back_, top_ = [[0, 0, 0] for _ in range(4)]
        left_ = [[0, 0, 0] for _ in range(3)]
        if direction == '+':
            for i in range(3):
                front_[i], bottom_[i], back_[i], top_[2-i] = top[i][0], front[i][0], bottom[i][0], back[i][0]
                for j in range(3):
                    left_[j][2-i] = left[i][j]
        else:
            for i in range(3):
                back_[2-i], bottom_[i], front_[i], top_[i] = top[i][0], back[i][0], bottom[i][0], front[i][0]
                for j in range(3):
                    left_[j][i] = left[i][j]

        for i in range(3):
            front[i][0], bottom[i][0], back[i][0], top[i][0] = front_[i], bottom_[i], back_[i], top_[i]
            for j in range(3):
                left[i][j] = left_[i][j]
    # 2. 앞 면이 돌아갔을 때
    # - 시계방향인 경우: 윗면의 아래 행 -> 오른쪽면의 왼쪽 열 -> 아랫면의 윗 행(역) -> 왼쪽면의 오른쪽 열 -> 윗면의 아래 행(역) 순으로 바뀐다.
    # - 반시계방향인 경우: 윗면의 아래 행 -> 왼쪽의 오른쪽 열(역) -> 아랫면의 윗 행 -> 오른쪽면의 왼쪽 열(역) -> 윗면의 아래 행 순으로 바뀐다.
    if order == 'F':
        right_, bottom_, left_, top_ = [[0, 0, 0] for _ in range(4)]
        front_ = [[0, 0, 0] for _ in range(3)]
        if direction == '+':
            for i in range(3):
                right_[i], bottom_[2-i], left_[i], top_[2-i] = top[2][i], right[i][0], bottom[0][i], left[i][2]
                for j in range(3):
                    front_[j][2-i] = front[i][j]
        else:
            for i in range(3):
                left_[2-i], bottom_[i], right_[2-i], top_[i] = top[2][i], left[i][2], bottom[0][i], right[i][0]
                for j in range(3):
                    front_[j][i] = front[i][j]

        for i in range(3):
            top[2][i], right[i][0], bottom[0][i], left[i][2] = top_[i], right_[i], bottom_[i], left_[i]
            for j in range(3):
                front[i][j] = front_[i][j]
    # 3. 오른쪽 면이 돌아갔을 때
    # - 시계방향인 경우: 윗면의 오른쪽 열 -> 뒷면의 오른쪽 열(역) -> 아랫면의 오른쪽 열 -> 앞면의 오른쪽 열 -> 윗면의 오른쪽 열 순으로 바뀐다.
    # - 반시계방향인 경우: 윗면의 오른쪽 열 -> 앞면의 오른쪽 열 -> 아랫면의 오른쪽 열 -> 뒷면의 오른쪽 열 -> 윗면의 오른쪽 열(역) 순으로 바뀐다.
    if order == 'R':
        front_, bottom_, back_, top_ = [[0, 0, 0] for _ in range(4)]
        right_ = [[0, 0, 0] for _ in range(3)]
        if direction == '+':
            for i in range(3):
                back_[2-i], bottom_[i], front_[i], top_[i] = top[i][2], back[i][2], bottom[i][2], front[i][2]
                for j in range(3):
                    right_[j][2-i] = right[i][j]
        else:
            for i in range(3):
                front_[2-i], bottom_[i], back_[i], top_[i] = top[i][2], front[i][2], bottom[i][2], back[i][2]
                for j in range(3):
                    right_[j][i] = right[i][j]
        for i in range(3):
            front[i][2], bottom[i][2], back[i][2], top[i][2] = front_[i], bottom_[i], back_[i], top_[i]
            for j in range(3):
                right[i][j] = right_[i][j]
    # 4. 윗면이 돌아갔을 때
    # - 시계방향인 경우: 왼쪽면의 윗 행 -> 뒷면의 아래행(역) -> 오른쪽면의 윗 행 -> 앞면의 윗행 -> 왼쪽면의 윗행순으로 바뀐다.
    # - 반시계방향인 경우: 왼쪽면의 윗 행 -> 앞면의 윗 행 -> 오른쪽면의 윗행 -> 뒷면의 아래행 -> 왼쪽면의 윗행(역)순으로 바뀐다.
    if order == 'U':
        back_, right_, front_, left_ = [[0, 0, 0] for _ in range(4)]
        top_ = [[0,0,0] for _ in range(3)]
        if direction == '+':
            for i in range(3):
                back_[2-i], right_[i], front_[i], left_[i] = left[0][i], back[2][i], right[0][i], front[0][i]
                for j in range(3):
                    top_[j][2-i] = top[i][j]
        else:
            for i in range(3):
                front_[i], right_[i], back_[i], left_[2-i] = left[0][i], front[0][i], right[0][i], back[0][i]
                for j in range(3):
                    top_[j][i] = top[i][j]

        for i in range(3):
            left[0][i], back[2][i], right[0][i], front[0][i] = left_[i], back_[i], right_[i], front_[i]
            for j in range(3):
                top[i][j] = top_[i][j]


    # 5. 아래 면이 돌아갔을 때
    # - 시계방향인 경우: 앞면의 아래 행 -> 오른쪽의 아래 행 -> 뒷면의 윗 행(역) -> 왼쪽면의 아래 행 -> 앞면의 아래 행
    # - 반시계방향인 경우: 앞면의 아래 행 -> 왼쪽면의 아래행 -> 뒷면의 윗 행 -> 오른쪽면의 아래 행(역) -> 앞면의 아래 행
    if order == 'D':
        back_, right_, front_, left_ = [[0, 0, 0] for _ in range(4)]
        bottom_ = [[0,0,0] for _ in range(3)]
        if direction == '+':
            for i in range(3):
                front_[i], right_[i], back_[2-i], left_[i] = left[2][i], front[2][i], right[2][i], back[0][i]
                for j in range(3):
                    bottom_[j][2-i] = bottom[i][j]
        else:
            for i in range(3):
                back_[i], right_[2-i], front_[i], left_[i] = left[2][i], back[0][i], right[2][i], front[2][i]
                for j in range(3):
                    bottom_[j][i] = bottom[i][j]

        for i in range(3):
            left[2][i], back[0][i], right[2][i], front[2][i] = left_[i], back_[i], right_[i], front_[i]
            for j in range(3):
                bottom[i][j] = bottom_[i][j]

    # 6. 뒷면이 돌아갔을 떄
    # - 시계방향인 경우: 아래면의 아래 행 -> 오른쪽면의 오른쪽 행 -> 윗면의 윗 행(역) -> 왼쪽면의 왼쪽 행 -> 아래면의 아래 행(역)
    # - 반시계방향인 경우: 아래면의 아래 행 -> 왼쪽면의 왼쪽 행(역) -> 윗면의 윗 행 -> 오른쪽면의 오른쪽 행(역) -> 아래면의 아래 행
    if order == 'B':
        bottom_, right_, top_, left_ = [[0, 0, 0] for _ in range(4)]
        back_ = [[0,0,0] for _ in range(3)]
        if direction == '+':
            for i in range(3):
                right_[i], top_[2-i], left_[i], bottom_[2-i] = bottom[2][i], right[i][2], top[0][i], left[i][0]
                for j in range(3):
                    back_[j][2-i] = back[i][j]
        else:
            for i in range(3):
                left_[2-i], top_[i], right_[2-i], bottom_[i] = bottom[2][i], left[i][0], top[0][i], right[i][2]
                for j in range(3):
                    back_[j][2-i] = back[i][j]

        for i in range(3):
            bottom[2][i], right[i][2], top[0][i], left[i][0] = bottom_[i], right_[i], top_[i], left_[i]
            for j in range(3):
                back[i][j] = back_[i][j]

    print('위:', top)
    print('왼:', left)
    print('앞:', front)
    print('오:', right)
    print('뒤:', back)
    print('바닥:', bottom)


for tc in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    orders = list(sys.stdin.readline().split())
    
    top = [['w' for _ in range(3)] for _ in range(3)]
    bottom = [['y' for _ in range(3)] for _ in range(3)]
    front = [['r' for _ in range(3)] for _ in range(3)]
    back = [['o' for _ in range(3)] for _ in range(3)]
    left = [['g' for _ in range(3)] for _ in range(3)]
    right = [['b' for _ in range(3)] for _ in range(3)]

    for i in range(n):
        cubing(orders[i][0], orders[i][1])
    print(top)