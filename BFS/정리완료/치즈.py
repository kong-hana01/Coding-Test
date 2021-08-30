# 접근 방법
# 0. 주어진 판을 입력받는다.(board) 또한 1의 위치를 모두 저장하고(cheese) 1의 개수를 따로 저장한다.(cheese_count)
# 1. 치즈 바깥 쪽에 있는 공기와 치즈 내부에 있는 구멍에 위치한 공기를 구분하기 위해 board의 첫번째 행, 첫번째 열에 위치한 공기를 기준으로 BFS를 동작해 1과 맞닿아있지 않은 값은 -1로 바꿔준다. (바깥쪽 공기) 
# 2-1. 이후 cheese를 하나씩 탐색하며 상하좌우의 위치 중 -1과 맞닿은 치즈를 따로 저장한다.(melting_cheese)
# 2-2. 또한 상하좌우에 -1과 0이 있다면 0은 BFS을 통해 -1로 값을 바꿔준다.
# 3. melting_cheese의 위치에 있는 치즈는 -1로 값을 바꾸고, melting_cheese의 개수만큼 cheese_count를 빼준다.
# 4. 2번과 3번을 cheese_count가 0이 될 때까지 반복한다.
# 5. 모든 치즈가 녹고 총 몇 번 반복했는지와 melting_cheese의 개수를 출력한다.

from collections import deque
import sys
input = sys.stdin.readline

# 0
row, col = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(row)]
cheese = []
for r in range(row):
    for c in range(col):
        if board[r][c] == 1:
            cheese.append([r, c])

# 1
def find_air(r, c):
    if board[r][c] == -1:
        return
    air = deque([])
    air.append([r, c])
    board[r][c] = -1
        
    while air:
        r, c = air.popleft()
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if 0<=r+dr<=row-1 and 0<=c+dc<=col-1 and board[r+dr][c+dc] == 0:
                air.append([r+dr, c+dc])
                board[r+dr][c+dc] = -1

find_air(0, 0)
time = 0
while True:
    if not len(cheese):
        break
    cheese_count = len(cheese)
    
    melting_cheese = []
    hole = []
    for r, c in cheese:
        check_air, check_hole = False, False
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if 0<=r+dr<=row-1 and 0<=c+dc<=col-1:
                if board[r+dr][c+dc] == -1 and not check_air:
                    melting_cheese.append([r, c])
                    check_air = True
                elif board[r+dr][c+dc] == 0:
                    check_hole = True
                    h = [r+dr, c+dc]
        if check_hole and check_air:
            hole.append(h)
    
    for r, c in hole:
        find_air(r, c)
    
    for r, c in melting_cheese:
        board[r][c] = -1

    rest_cheese = []
    for r, c in cheese:
        if board[r][c] == 1:
            rest_cheese.append([r, c])
    
    cheese = rest_cheese
    time += 1

print(time)
print(cheese_count)