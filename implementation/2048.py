# https://www.acmicpc.net/problem/12100
# 접근방법
# 주어진 보드에서 상하좌우로 총 5번씩 움직인 뒤, 나타난 결과 중 가장 큰 블록을 출력한다.
# 시간복잡도: 400(보드의 크기) x 4 ^ 5 (상하좌우를 총 5번 움직였을 때의 경우의 수) = 최대 약 410만번의 연산
import sys

n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 오른쪽으로 옮기기
for i in range(n):
    for j in range(n-1):
        if board[n-(i+1)][n-(j+1)] == board[n-(i+1)][n-(j+2)] != 0: # 이전 값과 같고 그 값이 0이 아닐 때 움직이는 방향의 값에 2를 곱한다.
            board[n-(i+1)][n-(j+1)] *= 2
            board[n-(i+1)][n-(j+2)] = 0

        elif board[n-(i+1)][n-(j+1)] == 0: # 값이 0일 때 해당 위치부터 왼쪽으로 차례로 탐색을 하며 0이 아닌 값이 존재한다면 그 값과 바꾼다.
            k = 2
            while n-(j+k) >= 0:
                if board[n-(i+1)][n-(j+k)] != 0:
                    board[n-(i+1)][n-(j+1)], board[n-(i+1)][n-(j+k)] = board[n-(i+1)][n-(j+k)], board[n-(i+1)][n-(j+1)]
                    # 값을 바꿨을 때, 해당 위치의 다음 값과 같을 경우 그 다음 값에 2를 곱한다.
                    if j > 0 and board[n-(i+1)][n-(j+1)] == board[n-(i+1)][n-j]:
                        board[n-(i+1)][n-j] *= 2
                        board[n-(i+1)][n-(j+1)] = 0
                    break
                k += 1
            
        print(board)


# 왼쪽으로 옮기기
for i in range(n):
    for j in range(n-1):
        if board[i][j] == board[i][j+1] != 0: # 이전 값과 같고 그 값이 0이 아닐 때 움직이는 방향의 값에 2를 곱한다.
            board[i][j] *= 2
            board[i][j+1] = 0

        elif board[i][j] == 0: # 값이 0일 때 해당 위치부터 왼쪽으로 차례로 탐색을 하며 0이 아닌 값이 존재한다면 그 값과 바꾼다.
            k = 1
            while j+k < n:
                if board[i][j+k] != 0:
                    board[i][j], board[i][j+k] = board[i][j+k], board[i][j]
                    # 값을 바꿨을 때, 해당 위치의 다음 값과 같을 경우 그 다음 값에 2를 곱한다.
                    if j > 0 and board[i][j] == board[i][j-1]:
                        board[i][j-1] *= 2
                        board[i][j] = 0
                    break
                k += 1
        # print(board)