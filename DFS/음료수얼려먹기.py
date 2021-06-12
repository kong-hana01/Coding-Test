n, m = 4, 5
condition = [input().split() for _ in range(n)]

"""
0 0 1 1 0
0 0 0 1 1
1 1 1 1 1
0 0 0 0 0
"""

#print(condition)
#condition = [[False, False, True, True, False], [False, False, False, True, True], [True, True, True, True, True], [False, False, False, False, False]]
ice_map = [[i, j] for i in range(n) for j in range(m)]

x, y = ice_map[1]


def ice_make(row, col, count=0, depth=0):
    """ x, y : 탐색지점 좌표
        count : 아이스크림 만들 수 있는 개수
    """
    condition[row][col] = 1
    
    for drow, dcol in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        if [row+drow, col+dcol] in ice_map:
            if not condition[row+drow][col+dcol]:
                #print(row+drow, col+dcol)
                ice_make(row+drow, col+dcol, count, depth+1)

    if depth == 0:
        count += 1
        for i in range(n):
            for j in range(m):
                if not condition[i][j]:
                    return ice_make(i, j, count)
        return count

print(ice_make(3, 0))
#print(condition[0][3])
#print(ice_make(0, 3))