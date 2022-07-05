# https://www.acmicpc.net/problem/16954
# 접근 방법
# 0. 총 8개의 움직이는 미로에 대한 모양을 board에 저장한다. 
# 1. BFS를 통해 몇 번 움직였는지에 대한 횟수와, 이동한 위치를 큐에 저장하여 board에 방문기록을 갱신한다.
# 2. 8번째로 움직였을 때 만약 이동할 수 있는 위치에 .이 있다면 1을 출력하고 이동할 수 없다면 0을 출력한다.
from collections import deque
import copy
board = [[[x for x in input()] for _ in range(8)]]
for _ in range(7):
    board.append([['.' for _ in range(8)]] + copy.deepcopy(board[-1][:7])) # 움직인 횟수를 index로 하는 board 초기화

queue = deque([]) # 큐 자료구조를 활용한 BFS
queue.append([0, 7, 0]) # 이동 횟수, x의 위치, y의 위치
is_arrive = False # 오른쪽 끝까지 갈 수 있는지 체크
while queue and not is_arrive:
    cnt, x, y = queue.popleft()
    for dx, dy in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]: # 움직일 수 있는 방향 설정
        if 0<=x+dx<=7 and 0<=y+dy<=7 and board[cnt+1][x+dx][y+dy] == '.': # 다음에 움직일 위치가 벽이 내려오지 않는 곳인 경우 동작
            if board[cnt][x+dx][y+dy] == '#':  # 움직일 수 있는 위치인지 확인
                continue
            queue.append([cnt+1, x+dx, y+dy])
            board[cnt+1][x+dx][y+dy] = 1
            if cnt+1 == 7: # 모든 벽이 내려온 뒤에는 더이상 탐색하지 않고 오른쪽 위로 이동할 수 있기에 is_arrive는 True
                is_arrive = True    
if is_arrive:
    print(1)
else:
    print(0)