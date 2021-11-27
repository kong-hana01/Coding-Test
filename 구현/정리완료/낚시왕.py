# https://www.acmicpc.net/problem/17143
# 접근방법
# 0. 상어에 대한 정보를 격자판에 입력한다. 각 격자판의 칸은 [속력, 이동 방향, 크기]를 입력한다.
# 1. 낚시왕이 오른쪽으로 한 칸씩 이동한 뒤, 해당 열에서 가장 적은 행에 위치한 상어를 잡는다.
# 2. 격자판을 하나씩 탐색하며 상어가 있는 칸이 나올 경우 이동방향과 속력에 따라 새로운 격자판에 해당 상어의 정보를 입력한다.
# 2-1. 새로운 격자판에 상어의 정보를 입력할 때 같은 칸에 상어가 존재한다면 크기가 큰 것만 입력한다.
# 2-2. 격자판을 새로 만들지 않을 경우 상어를 이동시켰을 때 이동을 시키지 않은 상어와 겹치면 2-1의 조건에 따라 이동을 시키지 않은 상어를 격자판에서 지울 수 있기 때문에 격자판을 새로 만들어야한다. 또한 이동했던 상어를 또 이동시킬 우려가 있다.
# 최대 연산 횟수: 칸의 개수 x 최대 반복 횟수 x 매 이동 시마다 사용할 격자판의 개수 = 10000 x 100 x 2 = 약 200만번


r, c, m = map(int, input().split())
grid = [[[0, 0, 0] for _ in range(c+1)] for _ in range(r+1)]

# 격자판에 상어 정보 입력 (0번 수행)
for _ in range(m):
    row, col, s, d, z = map(int, input().split())
    grid[row][col] = [s, d, z] 


def move(row, col, s, d):
    # 위
    if d == 1:
        if row - s >= 1:
            row -= s
        else:
            s -= row - 1
            direction = s // (r-1)
            location = s % (r-1)
            if direction % 2 == 0:
                d = 2
                row = 1 + location 
            else:
                row = r - location
    
    # 아래
    elif d == 2:
        if row + s <= r:
            row += s
        else:
            s -= r - row
            direction = s // (r-1)
            location = s % (r-1)
            if direction % 2 == 0:
                d = 1
                row = r - location 
            else:
                row = 1 + location
    
    # 오른쪽
    elif d == 3:
        if col + s <= c:
            col += s
        else:
            s -= c - col
            direction = s // (c-1)
            location = s % (c-1)
            if direction % 2 == 0:
                d = 4
                col = c - location 
            else:
                col = 1 + location

    # 왼쪽
    elif d == 4:
        if col - s >= 1:
            col -= s
        else:
            s -= col - 1
            direction = s // (c-1)
            location = s % (c-1)
            if direction % 2 == 0:
                d = 3
                col = 1 + location
            else:
                col = c - location 

    return row, col, d
            

def sharkMove():
    grid_ = [[[0, 0, 0] for _ in range(c+1)] for _ in range(r+1)]
    for row in range(1, r+1):
        for col in range(1, c+1):
            if grid[row][col] != [0, 0, 0]:
                s, d, z = grid[row][col]
                row_, col_, d = move(row, col, s, d)
                grid_[row_][col_] = max([s, d, z], grid_[row_][col_], key=lambda x: x[2])
                
    # for i in range(1, r+1):
    #     print(grid_[i][1:])
    # print()
    return grid_

result = 0
for time in range(1, c+1):
    for row in range(1, r+1):
        if grid[row][time] != [0, 0, 0]:
            result += grid[row][time][2]
            grid[row][time] = [0, 0, 0]
            break
    grid_ = sharkMove()
    grid = [x[:] for x in grid_]
    
    
print(result)