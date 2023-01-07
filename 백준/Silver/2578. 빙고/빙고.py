# https://www.acmicpc.net/problem/2578
def check():
    return row_check() + col_check() + diagonal_check()

def row_check():
    return list(map(lambda x: x.count(True) == 5, visited)).count(True)

def col_check():
    return sum([1 for i in range(5) if list(map(lambda x: x[i], visited)).count(True) == 5])

def diagonal_check():
    cnt1 = 0
    cnt2 = 0
    for r in range(5):
        c1 = r
        c2 = 4-r
        if visited[r][c1] == True:
            cnt1 += 1
        if visited[r][c2] == True:
            cnt2 += 1
    return [cnt1, cnt2].count(5)

board = [list(map(int, input().split())) for _ in range(5)]
numbers_index = [[] for _ in range(26)]
for r in range(5):
    for c in range(5):
        numbers_index[board[r][c]] = [r, c]
values = [list(map(int, input().split())) for _ in range(5)]
visited = [[False for _ in range(5)] for _ in range(5)]
cnt = 0
result = 0
for value in values:
    for x in value:
        cnt += 1
        r, c = numbers_index[x]
        visited[r][c] = True
        if check() >= 3:
            result = cnt
            break
    if result != 0:
        break
print(result)