# https://www.acmicpc.net/problem/2580
# 접근 방법
# 백트래킹을 사용해 문제를 해결한다.
sudoku = [list(map(int, input().split())) for _ in range(9)]
blank = []
columns = [set([]) for _ in range(9)]
rows = [set([]) for _ in range(9)]
boxs = [set([]) for _ in range(9)]
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            blank.append([i, j])
            continue
        columns[j].add(sudoku[i][j])
        rows[i].add(sudoku[i][j])
        boxs[i//3*3+j//3].add(sudoku[i][j])

def backtracking(idx):
    if idx == len(blank):
        return True
    r, c = blank[idx]
    for i in range(1, 10):
        if i not in columns[c] and i not in rows[r] and i not in boxs[r//3*3+c//3]:
            columns[c].add(i)
            rows[r].add(i)
            boxs[r//3*3+c//3].add(i)
            sudoku[r][c] = i
            if backtracking(idx+1):
                return True
            sudoku[r][c] = 0
            boxs[r//3*3+c//3].remove(i)
            columns[c].remove(i)
            rows[r].remove(i)
    return False

backtracking(0)
for i in range(9):
    print(*sudoku[i])