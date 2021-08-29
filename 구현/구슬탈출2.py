# https://www.acmicpc.net/problem/13460
# 백준 골드 문제
# 접근 방법
# 상하좌우로 기울인 위치를 큐에 삽입한다.
# 1. 처음 빨간구슬의 위치와 파란 구슬의 위치를 저장하고 그 위치를 .으로 바꾼다.
# 2. 빨간 구슬과 파란 구슬 중 기울인 방향에서 앞선 위치에 있는 구슬을 먼저 이동시킨다.
# 3. 이후 굴리지 않은 구슬을 이동방향으로 이동시킨다. 이때 굴린 구슬의 위치를 확인하며 같은 위치일 경우 이동하지 않고 멈춘다.
# 4. 만약 구슬을 굴리다 R 구슬이 구멍에 들어갈 경우 굴린 횟수를 출력한다.


# 최대 10번만 움직일 수 있기 때문에 상하좌위로 기울여서 움직인 위치와 움직인 횟수를 모두 queue에 삽입하고 빼면서 이를 계산한다.
# 연산횟수 : 최대 4^10 x 14= 1024 x 1024 x 14 = 약 1400만번




from collections import deque
import sys
n, m = map(int, sys.stdin.readline().split()) # 보드의 가로 세로 입력
board = [[x for x in sys.stdin.readline().rstrip()] for _ in range(n)] # 보드 정보 입력(연산 속도를 빠르게 하기 위해 문자열을 리스트로 변환)

for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            location_r = [i, j] # R의 처음 위치 초기화
            board[i][j] = '.' # 주어진 board에서의 R 위치를 .으로 바꾼다.
        elif board[i][j] == 'B':
            location_b = [i, j] # B의 처음 위치 초기화
            board[i][j] = '.' # 주어진 board에서의 B 위치를 .으로 바꾼다.


def move(location_r, location_b, direction):
    y_r, x_r = location_r
    y_b, x_b = location_b
    check = False
    fail = False
    if direction == 'up': # 위로 기울일 경우 -> 세로길이 -1
        if y_r <= y_b: # 빨간 구슬의 위치가 앞섰을 경우 빨간 구슬부터 탐색한다.
            while y_r > 0 and board[y_r - 1][x_r] != '#': # 빨간 구슬이 이동할 위치가 .인 경우 계속 이동한다.
                y_r -= 1
                if board[y_r][x_r] == 'O': # 빨간 구슬을 이동하다 구멍을 만나면 result에 count + 1을 저장하고 반복문을 끝낸다.
                    check = True
                    break

            while y_b > 0 and board[y_b - 1][x_b] != '#': # 파란 구슬이 이동할 위치가 .인 경우 계속 이동한다.
                if x_r == x_b and y_r == y_b - 1: # 단, 이동할 위치가 빨간 구슬과 겹치면 이동하지 않고 반복문을 멈춘다.
                    if check: # 파란 구슬과 빨간 구슬이 동시에 구멍에 들어간 경우
                        fail = True
                    break
                y_b -= 1
                if board[y_b][x_b] == 'O':
                    fail = True
                    break

        else: # 파란 구슬의 위치가 앞섰을 경우 파란 구슬부터 탐색한다.
            while y_b > 0 and board[y_b - 1][x_b] != '#': # 파란 구슬이 이동할 위치가 .인 경우 계속 이동한다.
                y_b -= 1
                if board[y_b][x_b] == 'O':
                    fail = True
                    break

            while y_r > 0 and board[y_r - 1][x_r] != '#': # 빨간 구슬이 이동할 위치가 .인 경우 계속 이동한다. 
                if x_r == x_b and y_r - 1 == y_b: # 단, 이동할 위치가 파란 구슬과 겹치면 이동하지 않고 반복문을 멈춘다.
                    break
                y_r -= 1           
                if board[y_r][x_r] == 'O': # 빨간 구슬을 이동하다 구멍을 만나면 result에 count + 1을 저장하고 반복문을 끝낸다.
                    check = True
                    break

    elif direction == 'down': # 아래로 기울일 경우 -> 세로길이 +1
        if y_r >= y_b: # 빨간 구슬의 위치가 앞섰을 경우 빨간 구슬부터 탐색한다.
            while y_r + 1 < n and board[y_r + 1][x_r] != '#': # 빨간 구슬이 이동할 위치가 .인 경우 계속 이동한다.
                y_r += 1
                if board[y_r][x_r] == 'O': # 빨간 구슬을 이동하다 구멍을 만나면 result에 count + 1을 저장하고 반복문을 끝낸다.
                    check = True
                    break

            while y_b + 1< n and board[y_b + 1][x_b] != '#': # 파란 구슬이 이동할 위치가 .인 경우 계속 이동한다.
                if x_r == x_b and y_r == y_b + 1: # 단, 이동할 위치가 빨간 구슬과 겹치면 이동하지 않고 반복문을 멈춘다.
                    if check: # 파란 구슬과 빨간 구슬이 동시에 구멍에 들어간 경우
                        fail = True
                    break
                y_b += 1
                if board[y_b][x_b] == 'O':
                    fail = True
                    break

        else: # 파란 구슬의 위치가 앞섰을 경우 파란 구슬부터 탐색한다.
            while y_b + 1 < n and board[y_b + 1][x_b] != '#': # 파란 구슬이 이동할 위치가 .인 경우 계속 이동한다.
                y_b += 1
                if board[y_b][x_b] == 'O':
                    fail = True
                    break

            while y_r + 1 < n and board[y_r + 1][x_r] != '#': # 빨간 구슬이 이동할 위치가 .인 경우 계속 이동한다. 
                if x_r == x_b and y_r + 1 == y_b: # 단, 이동할 위치가 파란 구슬과 겹치면 이동하지 않고 반복문을 멈춘다.
                    break
                y_r += 1           
                if board[y_r][x_r] == 'O': # 빨간 구슬을 이동하다 구멍을 만나면 result에 count + 1을 저장하고 반복문을 끝낸다.
                    check = True
                    break                

    elif direction == 'right': # 오른쪽으로 기울일 경우 -> 가로길이 +1
        if x_r >= x_b: # 빨간 구슬의 위치가 앞섰을 경우 빨간 구슬부터 탐색한다.
            while x_r + 1 < m and board[y_r][x_r + 1] != '#': # 빨간 구슬이 이동할 위치가 .인 경우 계속 이동한다.
                x_r += 1
                if board[y_r][x_r] == 'O': # 빨간 구슬을 이동하다 구멍을 만나면 result에 count + 1을 저장하고 반복문을 끝낸다.
                    check = True
                    break

            while x_b + 1 < m and board[y_b][x_b + 1] != '#': # 파란 구슬이 이동할 위치가 .인 경우 계속 이동한다.
                if x_r == x_b + 1 and y_r == y_b: # 단, 이동할 위치가 빨간 구슬과 겹치면 이동하지 않고 반복문을 멈춘다.
                    if check: # 파란 구슬과 빨간 구슬이 동시에 구멍에 들어간 경우
                        fail = True
                    break
                x_b += 1
                if board[y_b][x_b] == 'O':
                    fail = True
                    break

        else: # 파란 구슬의 위치가 앞섰을 경우 파란 구슬부터 탐색한다.
            while x_b + 1 < m and board[y_b][x_b + 1] != '#': # 파란 구슬이 이동할 위치가 .인 경우 계속 이동한다.
                x_b += 1
                if board[y_b][x_b] == 'O':
                    fail = True
                    break

            while x_r + 1 < m and board[y_r][x_r + 1] != '#': # 빨간 구슬이 이동할 위치가 .인 경우 계속 이동한다. 
                if x_r + 1 == x_b and y_r == y_b: # 단, 이동할 위치가 파란 구슬과 겹치면 이동하지 않고 반복문을 멈춘다.
                    break
                x_r += 1           
                if board[y_r][x_r] == 'O': # 빨간 구슬을 이동하다 구멍을 만나면 result에 count + 1을 저장하고 반복문을 끝낸다.
                    check = True
                    break   

    else: # 왼쪽으로 기울일 경우 -> 가로길이 -1
        if x_r <= x_b: # 빨간 구슬의 위치가 앞섰을 경우 빨간 구슬부터 탐색한다.
            while x_r > 0 and board[y_r][x_r - 1] != '#': # 빨간 구슬이 이동할 위치가 .인 경우 계속 이동한다.
                x_r -= 1
                if board[y_r][x_r] == 'O': # 빨간 구슬을 이동하다 구멍을 만나면 result에 count + 1을 저장하고 반복문을 끝낸다.
                    check = True
                    break

            while x_b > 0 and board[y_b][x_b - 1] != '#': # 파란 구슬이 이동할 위치가 .인 경우 계속 이동한다.
                if x_r == x_b - 1 and y_r == y_b: # 단, 이동할 위치가 빨간 구슬과 겹치면 이동하지 않고 반복문을 멈춘다.
                    if check: # 파란 구슬과 빨간 구슬이 동시에 구멍에 들어간 경우
                        fail = True
                    break
                x_b -= 1
                if board[y_b][x_b] == 'O':
                    fail = True
                    break

        else: # 파란 구슬의 위치가 앞섰을 경우 파란 구슬부터 탐색한다.
            while x_b > 0 and board[y_b][x_b - 1] != '#': # 파란 구슬이 이동할 위치가 .인 경우 계속 이동한다.
                x_b -= 1
                if board[y_b][x_b] == 'O':
                    fail = True
                    break

            while x_r > 0 and board[y_r][x_r - 1] != '#': # 빨간 구슬이 이동할 위치가 .인 경우 계속 이동한다. 
                if x_r - 1 == x_b and y_r == y_b: # 단, 이동할 위치가 파란 구슬과 겹치면 이동하지 않고 반복문을 멈춘다.
                    break
                x_r -= 1           
                if board[y_r][x_r] == 'O': # 빨간 구슬을 이동하다 구멍을 만나면 result에 count + 1을 저장하고 반복문을 끝낸다.
                    check = True
                    break
    location_r = [y_r, x_r]
    location_b = [y_b, x_b]
    # print(location_r, location_b)
    return location_r, location_b, check, fail

queue = deque([])
queue.append([location_r, location_b, 0, 0]) # 빨간 구슬의 위치, 파란 구슬의 위치, 카운트, 이동 방향
result = -1 # 결과값 초기화
while queue:
    location_r, location_b, count, ex_direction = queue.popleft()
    # print('현재 빨간 구슬 위치 :', location_r)
    # print('현재 파란 구슬 위치 :', location_b)
    if count == 10:
        break
    for direction in ['up', 'down', 'right', 'left']:
        if ex_direction == direction:
            continue
        new_r, new_b, check, fail = move(location_r, location_b, direction)
        if fail:
            continue
        elif check:
            print(count + 1)
            sys.exit()
        
        queue.append([new_r, new_b, count+1, direction])


print(result)