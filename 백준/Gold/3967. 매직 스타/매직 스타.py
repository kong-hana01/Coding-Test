# https://www.acmicpc.net/problem/3967
# 접근 방법
# 행과 열을 기준으로 A부터 L까지의 값을 채워가며 백트래킹을 해 문제를 해결한다.
alphaToNumber = {chr(alpha): alpha - ord('A') + 1 for alpha in range(ord("A"), ord("L")+1)}
numberToAlpha = {alpha - ord('A') + 1: chr(alpha) for alpha in range(ord("A"), ord("L")+1)}
board = [[x for x in input()] for _ in range(5)]
blank = []
check = [False for _ in range(13)]
lines = [[[0, 4], [1, 3], [2, 2], [3, 1]], 
        [[0, 4], [1, 5], [2, 6], [3, 7]],
        [[1, 1], [1, 3], [1, 5], [1, 7]],
        [[1, 1], [2, 2], [3, 3], [4, 4]],
        [[1, 7], [2, 6], [3, 5], [4, 4]],
        [[3, 1], [3, 3], [3, 5], [3, 7]]]

for r in range(5):
    for c in range(9):
        if board[r][c] == "x":
            blank.append([r, c])
        elif board[r][c] != '.':
            alpha = board[r][c]
            check[alphaToNumber[alpha]] = True

def backtracking(index):
    if index == len(blank):
        return True
    for i in range(1, 13):
        if not check[i]:
            r, c = blank[index]
            board[r][c] = numberToAlpha[i]
            if not bound(r, c):
                board[r][c] = 'x'
                continue

            check[i] = True
            if backtracking(index+1):
                return True
            check[i] = False
            board[r][c] = 'x'
    
    return False

def bound(r, c):
    for line in lines:
        if [r, c] in line:
            value = 0
            cnt = 0
            for r2, c2 in line:
                alpha = board[r2][c2]
                if alpha == 'x':
                    break
                cnt += 1
                value += alphaToNumber[alpha]
            if cnt == 4 and value != 26:
                return False
    return True

backtracking(0)
for x in board:
    print("".join(x))