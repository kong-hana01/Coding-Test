n, m = map(int, input().split())
condition = [input().split() for _ in range(n)]
ice_map = [[i, j] for i in range(n) for j in range(m)]

def ice_make(row, col):
    """ row, col : 탐색지점 좌표
        count : 아이스크림 만들 수 있는 개수
    """
    condition[row][col] = 1
    
    for drow, dcol in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        if [row+drow, col+dcol] in ice_map:
            if not condition[row+drow][col+dcol]:
                ice_make(row+drow, col+dcol)


count = 0
for i in range(n):
    for j in range(m):
        if not condition[i][j]:
            ice_make(i, j)
            count += 1
print(count)

