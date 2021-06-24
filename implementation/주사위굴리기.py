# 접근 방법
# 주사위의 좌우 방향에 대해 리스트를 따로 만들어서 매 명령마다 리스트의 값을 변경시켜준다.
# 명령의 최대 횟수는 1000번이다. 따라서 매 명령마다 리스트의 값을 바꾸더라도 각 리스트의 데이터가 4개이기 때문에 연산 횟수가 그리 많지 않다.

import sys
n, m, y, x, k = map(int, sys.stdin.readline().split())
array = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
orders = list(map(int, sys.stdin.readline().split()))

# 동쪽 : row 인덱스 포인트 -1 이동 
# 서쪽 : row 인덱스 포인트 1 이동 
# 북쪽 : column 인덱스 포인트 1 이동 
# 남쪽 : column 인덱스 포인트 -1 이동 

dice_row = [0, 0, 0, 0] # 아래, 서쪽 측면, 위, 동쪽 측면
dice_column = [0, 0, 0, 0] # 북쪽 측면, 위, 남쪽 측면, 아래

bottom_row = 0
top_row = 2

bottom_column = 3
top_column = 1


# 반복되는 문제이기에 함수처리
def copy_dice(x, y):

    # 만약 (x, y)의 좌표가 0이 아니라면, 칸에 쓰여 있는 수가 바닥으로 복사된다.
    if array[y][x] != 0:
        dice_column[bottom_column] = array[y][x]
        dice_row[bottom_row] = array[y][x]
        array[y][x] = 0

    # 만약 (x, y)의 좌표가 0이라면, 주사위 바닥이 칸으로 복사된다.
    else:
        array[y][x] = dice_column[bottom_column]
        array[y][x] = dice_row[bottom_row]


for order in orders:
    if order == 1:
        # x 좌표는 오른쪽으로 이동, 단 범위 밖으로 벗어나면 원상 복구 후, 반복문 break
        if x + 1 > m-1:
            continue 
        x += 1

        # 동쪽방향으로 이동 시, row 인덱스 포인트 -1만큼 이동
        bottom_row = (bottom_row - 1) % 4 
        top_row = (top_row - 1) % 4
        
        # 동쪽방향으로 이동 시, column 인덱스 변경 없이 위 아래 값만 변경
        dice_column[bottom_column] = dice_row[bottom_row]
        dice_column[top_column] = dice_row[top_row]

        copy_dice(x, y) # 주사위 바닥면 처리
        print(dice_row[top_row])

    elif order == 2:
        # x 좌표는 왼쪽으로 이동, 단 범위 밖으로 벗어나면 원상 복구 후, 반복문 break
        if x - 1 < 0:
            continue
        x -= 1

        # 서쪽방향으로 이동 시, row 인덱스 포인트 +1만큼 이동, 
        bottom_row = (bottom_row + 1) % 4 
        top_row = (top_row + 1) % 4

        # 서쪽방향으로 이동 시, column 인덱스 변경 없이 위 아래 값만 변경
        dice_column[bottom_column] = dice_row[bottom_row]
        dice_column[top_column] = dice_row[top_row]

        copy_dice(x, y) # 주사위 바닥면 처리
        print(dice_row[top_row])

    elif order == 3:
        # y 좌표는 위쪽으로 이동 단 범위 밖으로 벗어나면 원상 복구 후, 반복문 break
        if y - 1 < 0:
            continue
        y -= 1

        # 북쪽방향으로 이동 시, column 인덱스 포인트 +1만큼 이동
        bottom_column = (bottom_column + 1) % 4 
        top_column = (top_column + 1) % 4

        # 북쪽방향으로 이동 시, row 인덱스 변경 없이 위 아래 값만 변경
        dice_row[bottom_row] = dice_column[bottom_column]
        dice_row[top_row] = dice_column[top_column]

        copy_dice(x, y) # 주사위 바닥면 처리
        print(dice_row[top_row])

    elif order == 4:
        # y 좌표는 아래쪽으로 이동, 단 범위 밖으로 벗어나면 원상 복구 후, 반복문 break
        if y + 1 > n-1:
            continue
        y += 1

        # 남쪽방향으로 이동 시, column 인덱스 포인트 -1만큼 이동
        bottom_column = (bottom_column - 1) % 4 
        top_column = (top_column - 1) % 4

        # 남쪽방향으로 이동 시, row 인덱스 변경 없이 위 아래 값만 변경
        dice_row[bottom_row] = dice_column[bottom_column]
        dice_row[top_row] = dice_column[top_column]

        copy_dice(x, y) # 주사위 바닥면 처리
        print(dice_row[top_row])