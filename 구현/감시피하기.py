# https://www.acmicpc.net/problem/18428
# 접근 방법
# 모든 지점에 대해 장애물을 3개 설치해본 뒤 선생님이 학생을 볼 수 있는지 체크한다.
# 추후에 재귀로 다시 풀어보기



n = int(input())
board = [input().split() for _ in range(n)]
blank = []
teacher = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 'X':
            blank.append([i, j])
        elif board[i][j] == 'T':
            teacher.append([i, j])

for i in range(len(blank)):
    x1, y1 = blank[i]
    board[x1][y1] = 'O'
    for j in range(i+1, len(blank)):
        x2, y2 = blank[j]
        board[x2][y2] = 'O'
        for k in range(j+1, len(blank)):
            x3, y3 = blank[k]
            board[x3][y3] = 'O'
            result = True
            for tx, ty in teacher:
                for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    count = 1
                    while 0<= tx+dx*count <n and 0<= ty+dy*count <n and result:
                        if board[tx+dx*count][ty+dy*count] == 'S':
                            result = False
                        elif board[tx+dx*count][ty+dy*count] != 'X':
                            break
                        count += 1
            if result:
                break
            board[x3][y3] = 'X'
        if result:
            break
        board[x2][y2] = 'X'
    if result:
        break
    board[x1][y1] = 'X'

print('YES' if result else 'NO')
                    