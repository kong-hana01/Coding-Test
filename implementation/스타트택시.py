# https://www.acmicpc.net/problem/19238
# 접근 방법
# BFS를 활용해 승객을 태우고 목적지에 이동하는 과정을 구현한다.
# 최대 연산 횟수: 20x20x400x2 = 32만
from collections import deque

n, m, fuel = map(int, input().split())
map_ = [list(map(int, input().split())) for _ in range(n)]
taxi = list(map(int, input().split())) # 행, 열
passenger = [list(map(int, input().split())) for _ in range(m)] # 출발지 행, 열, 목적지 행, 열
board = [x[:] for x in map_]

for p in passenger:
    map_[p[0]-1][p[1]-1] = [p[2]-1, p[3]-1]

def moveToDeparture():
    # 현재 택시의 위치에서 가장 가까운 승객 탑승
    if type(map_[taxi[0]][taxi[1]]) != type([]):
        board_ = [x[:] for x in board]
        queue = deque([])
        queue.append([taxi[0], taxi[1], 0])

        passengerOnBoard = []
        result = 401
        while queue:
            row, col, cost = queue.popleft()
            for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                if 0<=row+dr<=n-1 and 0<=col+dc<=n-1:
                    if board_[row+dr][col+dc] == 0:
                        if type(map_[row+dr][col+dc]) == type([]):
                            passengerOnBoard.append([row+dr, col+dc, cost+1])
                            result = min(cost+1, result)

                        elif not passengerOnBoard:
                            queue.append([row+dr, col+dc, cost+1])
                            board_[row+dr][col+dc] = board_[row][col] + 1
        passengerOnBoard.sort(key=lambda x:(x[2], x[0], x[1]))
        return passengerOnBoard, result

    else:
        return [taxi], 0
    
def moveToDestination():
    # 현재 택시의 위치에서 목적지로 이동
    
    destination = map_[taxi[0]][taxi[1]]
    map_[taxi[0]][taxi[1]] = 0
    board_ = [x[:] for x in board]
    queue = deque([])
    queue.append([taxi[0], taxi[1]])
    
    cost = 0
    while queue:
        row, col = queue.popleft()
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if 0<=row+dr<=n-1 and 0<=col+dc<=n-1:
                if board_[row+dr][col+dc] == 0:
                    if [row+dr, col+dc] == destination:
                        queue = []
                        cost = board_[row][col] + 1
                        break
                    queue.append([row+dr, col+dc])
                    board_[row+dr][col+dc] = board_[row][col] + 1

    return destination, cost

taxi = [taxi[0]-1, taxi[1]-1]
for startTaxi in range(m):
    place, cost = moveToDeparture()
    if fuel < cost or not place:
        fuel = -1
        break
    fuel -= cost
    taxi = place[0][:2]
    place, cost = moveToDestination()
    if fuel < cost or cost == 0:
        fuel = -1
        break
    fuel += cost
    taxi = place

print(fuel)
